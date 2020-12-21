"""Users app serializers"""
from typing import Any, Dict, List, Type

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
        instance: User = super().create(validated_data)
        instance.set_password(validated_data["password"])
        instance.save()
        return instance
