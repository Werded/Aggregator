"""Currency models"""
from django.db import models
from django.utils.translation import gettext_lazy as _


class Currency(models.Model):
    """Currency model"""

    name: models.CharField = models.CharField(
        verbose_name=_("Name"),
        max_length=100,
        unique=True,
    )

    belarus_bank_code: models.CharField = models.CharField(
        verbose_name=_("Belarusbank Code"), max_length=50
    )

    def __str__(self) -> str:
        """Call as string"""
        return str(self.name)
