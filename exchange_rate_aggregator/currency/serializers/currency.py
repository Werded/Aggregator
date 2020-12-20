"""Currency serializers"""
from typing import List, Optional, Type

from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from exchange_rate_aggregator.currency.models import Currency, CurrencyHistory


class CurrencySerializer(serializers.ModelSerializer):
    """Currency model serializer"""

    current_rate_out: SerializerMethodField = SerializerMethodField()

    current_rate_in: SerializerMethodField = SerializerMethodField()

    class Meta:
        """Meta."""

        model: Type[Currency] = Currency
        fields: List[str] = [
            "id",
            "name",
            "current_rate_in",
            "current_rate_out",
        ]

    def get_current_rate_out(self, obj: Currency) -> Optional[float]:
        """Get Current rate"""
        last_rate: Optional[CurrencyHistory] = obj.currency_histories.order_by(
            "creation_date"
        ).last()
        return last_rate.rate_out if last_rate else None

    def get_current_rate_in(self, obj: Currency) -> Optional[float]:
        """Get Current rate"""
        last_rate: Optional[CurrencyHistory] = obj.currency_histories.order_by(
            "creation_date"
        ).last()
        return last_rate.rate_in if last_rate else None
