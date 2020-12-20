"""Currency app Urls"""
from typing import List

from django.urls import URLPattern

from rest_framework.routers import DefaultRouter

from exchange_rate_aggregator.currency.views import (
    CurrencyHistoryViewSet,
    CurrencyViewSet,
)

app_name: str = "currency"


router: DefaultRouter = DefaultRouter()

router.register(r"api/currencies", CurrencyViewSet, basename="currency")
router.register(
    r"api/currency_histories", CurrencyHistoryViewSet, basename="currency_history"
)

urlpatterns: List[URLPattern] = []
urlpatterns.extend(router.urls)
