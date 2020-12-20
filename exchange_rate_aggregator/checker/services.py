"""Checker app services"""
from typing import Any, Dict, List, Type

from exchange_rate_aggregator.checker.clients.base import BaseClient


class CheckerService:
    """Service for checking currency rates"""

    def __init__(self, client: Type[BaseClient]) -> None:
        """Init"""
        self.client = client()

    def check_rates(self) -> List:
        """Check current rates"""
        current_rates: Dict[str, Any] = self.client.get_rates()
        return self.client.create_history(current_rates)
