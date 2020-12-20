"""Users app serializers"""
from typing import Any, Dict, List, Type

from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

from exchange_rate_aggregator.users.models import User


class UserSerializer(serializers.ModelSerializer):
    """User model serializer"""

    class Meta:
        """Meta."""

        fields: List[str] = [
            "id",
            "email",
            "password",
        ]
        model: Type[User] = User
        extra_kwargs: Dict[str, Dict[str, Any]] = {
            "password": {"write_only": True},
        }

    def create(self, validated_data: dict) -> User:
        """Create users."""
        return User.objects.create_user(**validated_data)

    def validate_password(self, password: str) -> str:
        """Validate Password"""
        validate_password(password)
        return make_password(password)
