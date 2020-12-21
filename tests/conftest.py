import pytest
from faker import Faker
from rest_framework.test import APIClient

from tests.factories import UserFactory


@pytest.fixture
def faker():
    return Faker()


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture()
def client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client
