"""Authentication app serializers."""
from typing import Dict

from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ObtainTokenPairSerializer(TokenObtainPairSerializer):
    """Obtain token pair serializer."""

    def validate(self, attrs: dict) -> Dict[str, str]:
        """Validate serializer."""
        try:
            data: Dict[str, str] = super().validate(attrs)
        except AuthenticationFailed:
            raise AuthenticationFailed(_("Incorrect password or email"))

        return data
