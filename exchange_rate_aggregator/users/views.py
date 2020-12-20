"""Users app views"""
from typing import Type

from django.db.models import QuerySet

from exchange_rate_aggregator.core.views import BaseModelViewSet
from exchange_rate_aggregator.users.models import User
from exchange_rate_aggregator.users.serializers import UserSerializer


class UserViewSet(BaseModelViewSet):
    """ViewSet to viewing Users"""

    queryset: QuerySet = User.objects.all()
    serializer_class: Type[UserSerializer] = UserSerializer
