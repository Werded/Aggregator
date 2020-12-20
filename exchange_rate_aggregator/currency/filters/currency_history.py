"""Currency History filters"""
from datetime import date
from typing import Dict, List, Type

from django.db.models import QuerySet

from django_filters import DateTimeFromToRangeFilter, rest_framework
from django_filters.widgets import DateRangeWidget

from exchange_rate_aggregator.currency.models import CurrencyHistory


class CurrencyHistoryFilterSet(rest_framework.FilterSet):
    """Currency History FilterSet"""

    hour: rest_framework.NumberFilter = rest_framework.NumberFilter(
        method="filter_hour",
        label="Hour",
    )

    date_range: DateTimeFromToRangeFilter = DateTimeFromToRangeFilter(
        method="filter_date_range",
        label="Date range",
        widget=DateRangeWidget(attrs={"type": "date"}),
    )

    date_: rest_framework.DateFilter = rest_framework.DateFilter(
        method="filter_date",
        label="Date",
    )

    class Meta:
        """Meta."""

        model: Type[CurrencyHistory] = CurrencyHistory
        fields: Dict[str, List[str]] = {
            "currency": ["exact"],
        }

    def filter_hour(self, queryset: QuerySet, name: str, value: int) -> QuerySet:
        """Filter history by hour"""
        return queryset.filter(creation_date__hour=value)

    def filter_date_range(
        self, queryset: QuerySet, name: str, value: slice
    ) -> QuerySet:
        """Filter history between to dates"""
        return queryset.filter(
            creation_date__gte=value.start, creation_date__lte=value.stop
        )

    def filter_date(self, queryset: QuerySet, name: str, value: date) -> QuerySet:
        """Filter history by date"""
        return queryset.filter(
            creation_date__day=value.day,
            creation_date__year=value.year,
            creation_date__month=value.month,
        )
