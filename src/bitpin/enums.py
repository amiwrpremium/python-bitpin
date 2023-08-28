"""
# Enums.

Enum classes for the BitPin API.
"""

from typing import Any, List
from enum import (
    Enum as _Enum,
    EnumMeta as _EnumMeta,
)


class EnumMeta(_EnumMeta):
    """Enum Meta."""

    def __call__(cls, value: Any, *args: Any, **kwargs: Any) -> "Enum":  # type: ignore[override]
        """Call."""
        if isinstance(value, str):  # pragma: no cover
            value = value.upper()

        return super().__call__(value, *args, **kwargs)  # type: ignore[no-any-return]  # noqa

    def __contains__(cls, value: Any) -> bool:
        """Contains."""

        if isinstance(value, str):
            return value.upper() in cls._value2member_map_  # type: ignore[attr-defined]  # noqa

        return super().__contains__(value)  # type: ignore[call-arg]  # noqa


class Enum(_Enum, metaclass=EnumMeta):
    """Enum."""

    def __repr__(self) -> str:
        """
        Representation.

        Returns:
            str: Representation.
        """

        return f"{self.__class__.__name__}.{self.name}"

    def __str__(self) -> str:
        """
        String representation.

        Returns:
            str: String representation.
        """

        return str(self.value)

    def __eq__(self, other: Any) -> bool:  # pragma: no cover
        """
        Equal.

        Args:
            other (Any): Other.

        Returns:
            bool: True if equal, else False.
        """

        if isinstance(other, Enum):
            return self.value == other.value  # type: ignore[no-any-return]  # noqa
        return self.value == other  # type: ignore[no-any-return]  # noqa

    def __hash__(self) -> int:  # pragma: no cover
        """
        Hash.

        Returns:
            int: Hash.
        """

        return hash(self.value)

    @classmethod
    def _missing_(cls, value: object) -> "Enum":
        """
        Missing.

        Args:
            value (object): Value.

        Returns:
            Enum: Enum.
        """

        for member in cls:
            if isinstance(value, str) and member.value == value.upper():  # pragma: no cover
                return member

        return super()._missing_(value)  # type: ignore[attribute-error, no-any-return]  # noqa

    @classmethod
    def get_by_value(cls, value: Any) -> "Enum":
        """
        Get Enum by value.

        Args:
            value (Any): Value.

        Returns:
            Enum: Enum.
        """

        for enum in cls:
            if enum.value.lower() == value.lower():
                return enum
        raise ValueError(f"Invalid value: {value}")

    @classmethod
    def get_by_name(cls, name: Any) -> "Enum":
        """
        Get Enum by name.

        Args:
            name (Any): Name.

        Returns:
            Enum: Enum.
        """

        for enum in cls:
            if enum.name.lower() == name.lower():
                return enum
        raise ValueError(f"Invalid name: {name}")

    @classmethod
    def get_by_name_or_value(cls, name_or_value: Any) -> "Enum":
        """
        Get Enum by name or value.

        Args:
            name_or_value (Any): Name or value.

        Returns:
            Enum: Enum.
        """

        try:
            return cls.get_by_name(name_or_value)
        except ValueError:
            return cls.get_by_value(name_or_value)

    @classmethod
    def get_all_values(cls) -> List[Any]:
        """Get all values."""
        return [enum.value for enum in cls]

    @classmethod
    def get_all_names(cls) -> List[str]:
        """Get all names."""
        return [enum.name for enum in cls]

    @classmethod
    def to_django_choices(cls) -> List[tuple]:
        """Get all names."""
        return [(enum.name, enum.name) for enum in cls]


class OrderType(str, Enum):
    """Order Type (BUY/SELL)."""

    BUY = "buy"
    SELL = "sell"


class OrderMode(str, Enum):
    """Order Mode (LIMIT/MARKET/OCO/STOP_LIMIT)."""

    LIMIT = "limit"
    MARKET = "market"
    OCO = "oco"
    STOP_LIMIT = "stop_limit"


class OrderState(str, Enum):
    """Order State (INITIAL/ACTIVE/CLOSED)."""

    INITIAL = "initial"
    ACTIVE = "active"
    CLOSED = "closed"


class RequestMethod(str, Enum):
    """Request Methods (GET/POST/PUT/DELETE)."""

    GET = "get"
    POST = "post"
    PUT = "put"
    DELETE = "delete"
