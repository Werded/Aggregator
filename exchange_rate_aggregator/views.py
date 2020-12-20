"""Universal Start view."""
from typing import Dict

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from exchange_rate_aggregator import __version__


class IndexView(View):
    """Start page view"""

    def get(self, request: HttpRequest) -> HttpResponse:
        """Get root."""
        context: Dict[str, str] = {"version": __version__}
        return render(request, "index.html", context)


schema_view = get_schema_view(
    openapi.Info(
        title="Exchange Rate Aggregator API",
        default_version=__version__,
        description="Backend",
        contact=openapi.Contact(email="werded@tut.by"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
