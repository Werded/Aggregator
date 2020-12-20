"""Checker app config"""
from django.apps import AppConfig


class CheckerConfig(AppConfig):
    """App config"""

    name: str = "exchange_rate_aggregator.checker"
