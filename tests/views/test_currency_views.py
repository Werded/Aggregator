import pytest
from rest_framework import status

from exchange_rate_aggregator.currency.views import CurrencyViewSet
from tests.factories import CurrencyFactory


@pytest.mark.django_db
def test_currency_list(rf, user):
    currency = CurrencyFactory.create()
    request = rf.get("")
    response = CurrencyViewSet.as_view({"get": "list"})(request)
    assert response.status_code == status.HTTP_200_OK
    assert response.data[0]["id"] == currency.id


@pytest.mark.django_db
def test_currency_detail(rf, user):
    currency = CurrencyFactory.create()
    request = rf.get("")
    response = CurrencyViewSet.as_view({"get": "retrieve"})(request, pk=currency.pk)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == currency.id
