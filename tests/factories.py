import factory
from factory.django import DjangoModelFactory

from exchange_rate_aggregator.currency.models import Currency, CurrencyHistory
from exchange_rate_aggregator.users.models import User


class UserFactory(DjangoModelFactory):
    """User factory."""

    class Meta:
        """Meta."""

        model = User

    email = factory.Faker("email")
    password = factory.Faker("password", length=8)


class CurrencyFactory(DjangoModelFactory):
    class Meta:
        """Meta."""

        model = Currency

    name = factory.Faker("currency_name")
    belarus_bank_code = factory.Faker("currency_code")


class CurrencyHistoryFactory(DjangoModelFactory):
    class Meta:
        """Meta."""

        model = CurrencyHistory

    currency = factory.SubFactory(CurrencyFactory)
    rate_out = factory.Faker("pyfloat", positive=True, min_value=0, right_digits=2)
    rate_in = factory.Faker("pyfloat", positive=True, min_value=0, right_digits=2)
