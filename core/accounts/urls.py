from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from core.accounts.views import UserViewSet, ProfileViewSet
from core.accounts.views.auth import (
    RegisterView,
    LoginView,
    MeView,
    ForgotPasswordView,
)

from core.accounts.views.dashboard import DashboardSummaryView

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"profiles", ProfileViewSet, basename="profile")

urlpatterns = [
    path("", include(router.urls)),

    # AUTH
    path("auth/register/", RegisterView.as_view()),
    path("auth/login/", LoginView.as_view()),
    path("auth/me/", MeView.as_view()),
    path("auth/forgot-password/", ForgotPasswordView.as_view()),
    path("auth/token/refresh/", TokenRefreshView.as_view()),

    # DASHBOARD
    path("dashboard/summary/", DashboardSummaryView.as_view()),
]