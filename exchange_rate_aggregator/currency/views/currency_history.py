"""Currency History Views"""
from typing import Tuple, Type

from django.db.models import QuerySet

from rest_framework.permissions import BasePermission, IsAuthenticated

from exchange_rate_aggregator.core.views import BaseReadOnlyViewSet
from exchange_rate_aggregator.currency.filters import CurrencyHistoryFilterSet
from exchange_rate_aggregator.currency.models import CurrencyHistory
from exchange_rate_aggregator.currency.serializers import CurrencyHistorySerializer


class CurrencyHistoryViewSet(BaseReadOnlyViewSet):
    """ViewSet to viewing Currency History"""

    queryset: QuerySet = CurrencyHistory.objects.all()
    serializer_class: Type[CurrencyHistorySerializer] = CurrencyHistorySerializer
    permission_classes: Tuple[Type[BasePermission], ...] = (IsAuthenticated,)
    filterset_class: Type[CurrencyHistoryFilterSet] = CurrencyHistoryFilterSet
