from django.core.cache import cache
from django.db import connections
from django.db.utils import OperationalError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes([AllowAny])
def live_check(request):
    return Response({"status": "alive"})


@api_view(["GET"])
@permission_classes([AllowAny])
def ready_check(request):
    db_ok = True
    cache_ok = True

    try:
        connections["default"].cursor()
    except OperationalError:
        db_ok = False

    try:
        cache.set("healthcheck", "ok", timeout=5)
        cache_ok = cache.get("healthcheck") == "ok"
    except Exception:
        cache_ok = False

    status_code = 200 if db_ok and cache_ok else 503

    return Response(
        {
            "status": "ready" if status_code == 200 else "not_ready",
            "database": db_ok,
            "cache": cache_ok,
        },
        status=status_code,
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def health_check(request):
    return ready_check(request)