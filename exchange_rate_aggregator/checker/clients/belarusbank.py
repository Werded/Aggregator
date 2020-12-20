"""BelarusBank client"""
import logging
from typing import Any, Dict, List

from django.conf import settings
from django.utils import timezone

from requests import Response

from exchange_rate_aggregator.checker.clients.base import BaseClient
from exchange_rate_aggregator.currency.models import Currency, CurrencyHistory

logger = logging.getLogger(__name__)


class BelarusBankClient(BaseClient):
    """BelarusBank API client"""

    BASE_URL = settings.BELARUS_BANK_URL
    CURRENCY_LIST: List[str] = [
        "USD",
        "EUR",
        "RUB",
        "GBP",
        "CAD",
        "PLN",
        "UAH",
        "SEK",
        "CHF",
        "JPY",
        "CNY",
        "CZK",
        "NOK",
    ]

    def get_rates(self) -> Dict[str, Any]:
        """Get BelarusBank currency rates"""
        response: Response = self.send_request(params={"city": "Минск"})
        data: Dict[str, Any] = self.prepare_data(response.json()[0])
        return data

    def prepare_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Prepare BelarusBank rate data"""
        new_data: Dict = {}
        for currency in self.CURRENCY_LIST:
            new_data.update(
                {
                    currency: {
                        "in": data[f"{currency}_in"],
                        "out": data[f"{currency}_out"],
                    },
                }
            )
        return new_data

    def create_history(self, current_rates: Dict[str, Any]) -> List:
        """Create Currency History objects from rates data"""
        history_records: List = []
        for currency in Currency.objects.iterator():

            try:
                history_record: CurrencyHistory = CurrencyHistory(
                    currency=currency,
                    rate_in=current_rates[currency.belarus_bank_code]["in"],
                    rate_out=current_rates[currency.belarus_bank_code]["out"],
                    creation_date=timezone.now(),
                )
                history_records.append(history_record)

            except KeyError as e:
                logger.warning(msg=e)

        return CurrencyHistory.objects.bulk_create(history_records)
