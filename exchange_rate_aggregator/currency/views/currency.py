"""Currency Views"""
from typing import Type

from django.db.models import QuerySet

from exchange_rate_aggregator.core.views import BaseReadOnlyViewSet
from exchange_rate_aggregator.currency.models import Currency
from exchange_rate_aggregator.currency.serializers import CurrencySerializer


class CurrencyViewSet(BaseReadOnlyViewSet):
    """ViewSet to viewing Currencies """

    queryset: QuerySet = Currency.objects.all()
    serializer_class: Type[CurrencySerializer] = CurrencySerializer
