"""Currency History models"""
from django.db import models
from django.utils.translation import gettext_lazy as _


class CurrencyHistory(models.Model):
    """Currency History model"""

    currency: models.ForeignKey = models.ForeignKey(
        to="currency.Currency",
        on_delete=models.CASCADE,
        related_name="currency_histories",
        verbose_name=_("Currency"),
    )

    rate_out: models.FloatField = models.FloatField(verbose_name=_("Rate out"))

    rate_in: models.FloatField = models.FloatField(verbose_name=_("Rate in"))

    creation_date: models.DateTimeField = models.DateTimeField(
        verbose_name=_("Creation date"),
        auto_now_add=True,
    )

    def __str__(self) -> str:
        """Call as string"""
        return f"Rate of {self.currency} on {self.creation_date}"
