"""Base client"""
from typing import Any, Dict, List, Optional

import requests
from requests import Response
from rest_framework.exceptions import APIException


class ClientException(APIException):
    """Client Exception"""

    pass


class BaseClient:
    """Base API Client"""

    BASE_URL: str

    def send_request(
        self, params: Optional[Dict] = None, headers: Optional[Dict] = None
    ) -> Response:
        """Sends requests to bank API"""
        response: Response = requests.get(self.BASE_URL, params=params, headers=headers)
        if response.status_code != 200:
            raise ClientException(
                detail=f"{self.__name__} exception", code=response.status_code
            )

        return response

    def get_rates(self) -> Dict[str, Any]:
        """Get rates for currency"""
        raise NotImplementedError("get_rates must be implemented")

    def prepare_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Prepare rate data"""
        raise NotImplementedError("prepare_data must be implemented")

    def create_history(self, current_rates: Dict[str, Any]) -> List:
        """Create Currency History"""
        raise NotImplementedError("create_history must be implemented")
