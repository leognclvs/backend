from decouple import config, Csv
from django.http import JsonResponse


class RequestFirewallMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_ips = set(config("FIREWALL_ALLOWED_IPS", default="", cast=Csv()))
        self.blocked_ips = set(config("FIREWALL_BLOCKED_IPS", default="", cast=Csv()))
        self.blocked_agents = [
            agent.strip().lower()
            for agent in config("FIREWALL_BLOCKED_AGENTS", default="curl,sqlmap,nmap", cast=Csv())
            if agent.strip()
        ]
        self.blocked_paths = [
            pattern.strip().lower()
            for pattern in config(
                "FIREWALL_BLOCKED_PATHS",
                default="/.env,/wp-admin,/phpmyadmin,/server-status",
                cast=Csv(),
            )
            if pattern.strip()
        ]

    def __call__(self, request):
        client_ip = self._extract_client_ip(request)
        path = request.path.lower()
        user_agent = request.META.get("HTTP_USER_AGENT", "").lower()

        if self.allowed_ips and client_ip not in self.allowed_ips:
            return self._deny("IP nao autorizada pelo firewall.")

        if client_ip in self.blocked_ips:
            return self._deny("IP bloqueada pelo firewall.")

        if any(pattern in user_agent for pattern in self.blocked_agents):
            return self._deny("User-Agent bloqueado pelo firewall.")

        if any(path.startswith(pattern) for pattern in self.blocked_paths):
            return self._deny("Rota bloqueada pelo firewall.")

        response = self.get_response(request)
        response["X-Firewall-Status"] = "active"
        return response

    def _extract_client_ip(self, request):
        forwarded = request.META.get("HTTP_X_FORWARDED_FOR", "")
        if forwarded:
            return forwarded.split(",")[0].strip()
        return request.META.get("REMOTE_ADDR", "")

    def _deny(self, reason):
        return JsonResponse(
            {
                "detail": reason,
                "code": "firewall_blocked",
            },
            status=403,
        )
