"""Core app validators"""
import re
from typing import Dict, Match, Optional

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from exchange_rate_aggregator.users.models import User


class BaseValidator:
    """Base Validator"""

    pattern: str
    message: str
    params: Dict

    def __init__(self, min_symbols: int = 1) -> None:
        """Init"""
        self.min_symbols: int = min_symbols

    def validate(self, password: str, user: Optional[User] = None) -> None:
        """Validate"""
        result: Optional[Match[str]] = re.search(self.pattern, password)
        if not result:
            raise ValidationError(
                _(self.message),
                params={"min_symbols": self.min_symbols},
            )

    def get_help_text(self) -> str:
        """Get help text"""
        return _(
            "You password has to contains minimum %(min_symbols)d special symbols"
            % {"min_symbols": self.min_symbols}
        )


class SpecialSymbolMinimumValidator(BaseValidator):
    """Validate whether the password is contains special symbols"""

    def __init__(self, min_symbols: int = 1) -> None:
        """Init"""
        super().__init__(min_symbols)
        self.pattern: str = r"\W" + f"{{{self.min_symbols}}}"
        self.message: str = (
            "This password must contain at least %(min_symbols)d special symbols."
        )


class AlphaMinimumValidator(BaseValidator):
    """Validate whether the password is contains alphabet characters"""

    def __init__(self, min_symbols: int = 2) -> None:
        """Init"""
        super().__init__(min_symbols)
        self.pattern: str = r"[a-zA-Z]" + f"{{{self.min_symbols}}}"
        self.message: str = (
            "This password must contain at least %(min_symbols)d alphabet characters."
        )


class DigestMinimumValidator(BaseValidator):
    """Validate whether the password is contains alphabet characters"""

    def __init__(self, min_symbols: int = 2) -> None:
        """Init"""
        super().__init__(min_symbols)
        self.pattern: str = r"\d" + f"{{{self.min_symbols}}}"
        self.message: str = (
            "This password must contain at least %(min_symbols)d numeric characters."
        )
