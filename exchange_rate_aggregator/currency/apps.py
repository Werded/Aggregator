"""Currency app config"""
from django.apps import AppConfig


class CurrencyConfig(AppConfig):
    """App config"""

    name: str = "exchange_rate_aggregator.currency"
