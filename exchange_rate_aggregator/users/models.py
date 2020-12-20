"""Users app models"""
from typing import Any, List, Optional

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """User manager."""

    def _create_user(self, email: str, password: str, **extra_fields: Any):
        """Create and save a users with the given email, and password."""
        normalized_email: str = self.normalize_email(email)
        user: User = self.model(email=normalized_email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email: str, password: str, **extra_fields: Any):
        """Create users."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user: User = self._create_user(
            email=email,
            password=password,
            **extra_fields,
        )
        return user


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

    objects: UserManager = UserManager()

    USERNAME_FIELD: str = "email"
    REQUIRED_FIELDS: List[str] = []

    def __str__(self) -> str:
        """Call as string."""
        return str(self.email)
