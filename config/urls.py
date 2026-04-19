from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from core.common.health import health_check, ready_check, live_check

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/v1/", include("config.api_router")),

    path("api/v1/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("api/v1/", include("core.accounts.urls")),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),

    path("health/", health_check, name="health"),
    path("health/live/", live_check, name="health-live"),
    path("health/ready/", ready_check, name="health-ready"),
    
]