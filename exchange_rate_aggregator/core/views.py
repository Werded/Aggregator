"""Core app views"""
from typing import List

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet


class BaseView:
    """Base View"""

    ordering: List[str] = ["id"]


class BaseReadOnlyViewSet(BaseView, ReadOnlyModelViewSet):
    """Base Read Only ViewSet"""

    pass


class BaseModelViewSet(BaseView, ModelViewSet):
    """Base Read Only ViewSet"""

    pass
