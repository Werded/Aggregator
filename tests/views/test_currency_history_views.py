import pytest
from rest_framework import status
from rest_framework.test import force_authenticate

from exchange_rate_aggregator.currency.views import CurrencyHistoryViewSet
from tests.factories import CurrencyHistoryFactory


@pytest.mark.django_db
def test_currency_history_list(rf, user):

    history = CurrencyHistoryFactory.create()
    request = rf.get("")
    force_authenticate(request, user)
    response = CurrencyHistoryViewSet.as_view({"get": "list"})(request)
    assert response.status_code == status.HTTP_200_OK
    assert response.data[0]["id"] == history.id


@pytest.mark.django_db
def test_currency_history_list_fail(rf, user):

    CurrencyHistoryFactory.create()
    request = rf.get("")
    response = CurrencyHistoryViewSet.as_view({"get": "list"})(request)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_currency_history_detail(rf, user):

    history = CurrencyHistoryFactory.create()
    request = rf.get("")
    force_authenticate(request, user)
    response = CurrencyHistoryViewSet.as_view({"get": "retrieve"})(
        request, pk=history.pk
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == history.id


@pytest.mark.django_db
def test_currency_history_detail_fail(rf, user):

    history = CurrencyHistoryFactory.create()
    request = rf.get("")
    response = CurrencyHistoryViewSet.as_view({"get": "retrieve"})(
        request, pk=history.pk
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
