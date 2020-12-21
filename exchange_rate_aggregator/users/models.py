"""Users app models"""
from typing import List, Optional

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """User model"""

    username: Optional[models.CharField] = None

    email: models.EmailField = models.EmailField(
        verbose_name=_("Email"),
        unique=True,
    )

    google_id: models.CharField = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    USERNAME_FIELD: str = "email"
    REQUIRED_FIELDS: List[str] = []

    def __str__(self) -> str:
        """Call as string."""
        return str(self.email)
