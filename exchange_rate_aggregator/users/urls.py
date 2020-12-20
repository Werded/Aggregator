"""Users app urls"""
from typing import List

from django.urls import URLPattern

from rest_framework.routers import DefaultRouter

from exchange_rate_aggregator.users.views import UserViewSet

app_name: str = "users"


router: DefaultRouter = DefaultRouter()

router.register(r"api/users", UserViewSet, basename="user")

urlpatterns: List[URLPattern] = []
urlpatterns.extend(router.urls)
