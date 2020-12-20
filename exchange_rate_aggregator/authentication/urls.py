"""Authentication app urls"""
from typing import List

from django.urls import URLPattern, path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from exchange_rate_aggregator.authentication.serializers import (
    ObtainTokenPairSerializer,
)

app_name: str = "authentication"

urlpatterns: List[URLPattern] = [
    path("auth/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    path(
        "auth/token/",
        TokenObtainPairView.as_view(serializer_class=ObtainTokenPairSerializer),
        name="obtain_token",
    ),
]
