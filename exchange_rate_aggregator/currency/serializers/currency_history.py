"""Currency History serializers"""
from typing import List, Type

from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from exchange_rate_aggregator.currency.models import CurrencyHistory


class CurrencyHistorySerializer(serializers.ModelSerializer):
    """Currency History model serializer"""

    currency_name: SerializerMethodField = SerializerMethodField()

    class Meta:
        """Meta."""

        model: Type[CurrencyHistory] = CurrencyHistory
        fields: List[str] = [
            "id",
            "currency",
            "currency_name",
            "creation_date",
            "rate_in",
            "rate_out",
        ]

    def get_currency_name(self, obj: CurrencyHistory) -> str:
        """Get currency name"""
        return obj.currency.name
