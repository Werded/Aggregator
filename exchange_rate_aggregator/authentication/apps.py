"""Authentication apps"""
from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """Authentication config."""

    name: str = "exchange_rate_aggregator.authentication"
