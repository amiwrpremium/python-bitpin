"""
# Types.

Types for Python Bitpin.

## Description
This file contains all the types used in the project.
"""

import typing as t
import asyncio
import requests
import aiohttp

from . import enums

# General Types:
OptionalStr = t.Optional[str]
OptionalInt = t.Optional[int]
OptionalFloat = t.Optional[float]

DictStrAny = t.Dict[str, t.Any]
OptionalDictStrAny = t.Optional[DictStrAny]

EventLoop = asyncio.AbstractEventLoop
OptionalEventLoop = t.Optional[EventLoop]

# Client Types:
OrderTypeBuy = t.Literal["buy"]
OrderTypeSell = t.Literal["sell"]
OrderTypes = t.Union[OrderTypeBuy, OrderTypeSell, enums.OrderType]
OptionalOrderTypes = t.Optional[OrderTypes]

OrderModeLimit = t.Literal["limit"]
OrderModeMarket = t.Literal["market"]
OrderModeOCO = t.Literal["oco"]
OrderModeStopLimit = t.Literal["stop_limit"]
OrderModes = t.Union[OrderModeLimit, OrderModeMarket, OrderModeOCO, OrderModeStopLimit, enums.OrderMode]
OptionalOrderModes = t.Optional[OrderModes]

# HTTP Types:
HttpSession = t.Union[requests.Session, aiohttp.ClientSession]
HttpResponses = t.Union[requests.Response, aiohttp.ClientResponse]

# Request Types:
RequestMethodGet = t.Literal["get"]
RequestMethodPost = t.Literal["post"]
RequestMethodPut = t.Literal["put"]
RequestMethodDelete = t.Literal["delete"]
RequestMethods = t.Union[
    RequestMethodGet,
    RequestMethodPost,
    RequestMethodPut,
    RequestMethodDelete,
    enums.RequestMethod,
]

# Response Types:
ResultListResponse = t.TypedDict(
    "ResultListResponse",
    {
        "count": t.Optional[int],
        "next": t.Optional[str],
        "previous": t.Optional[str],
        "results": t.List[DictStrAny],
    },
)

InnerOrderbookResponse = t.TypedDict(
    "InnerOrderbookResponse",
    {
        "amount": str,
        "price": str,
        "remain": str,
        "value": str,
    },
)

OrderbookResponse = t.TypedDict("OrderbookResponse", {"orders": t.List[InnerOrderbookResponse], "volume": str})

InnerTradeResponse = t.TypedDict(
    "InnerTradeResponse",
    {
        "time": float,
        "price": str,
        "value": str,
        "match_amount": str,
        "type": str,
        "match_id": str,
    },
)

TradeResponse = t.List[InnerTradeResponse]

LoginResponse = t.TypedDict(
    "LoginResponse",
    {
        "refresh": str,
        "access": str,
    },
)

RefreshTokenResponse = t.TypedDict(
    "RefreshTokenResponse",
    {
        "access": str,
    },
)

CurrencyInfo = t.TypedDict(
    "CurrencyInfo",
    {
        "id": int,
        "title": str,
        "title_fa": str,
        "code": str,
        "tradable": bool,
        "for_test": bool,
        "image": str,
        "decimal": int,
        "decimal_amount": int,
        "decimal_irt": int,
        "color": str,
        "high_risk": bool,
        "show_high_risk": bool,
        "withdraw_commission": str,
        "tags": t.List[DictStrAny],
    },
)

WalletInfo = t.TypedDict(
    "WalletInfo",
    {
        "id": int,
        "currency": CurrencyInfo,
        "balance": str,
        "frozen": str,
        "total": str,
        "value": str,
        "value_frozen": str,
        "value_total": str,
        "usdt_value": str,
        "usdt_value_frozen": str,
        "usdt_value_total": str,
        "address": str,
        "inviter_commission": str,
        "service": str,
        "daily_withdraw": str,
    },
)

MarketInfo = t.TypedDict(
    "MarketInfo",
    {
        "id": int,
        "currency1": CurrencyInfo,
        "currency2": CurrencyInfo,
        "code": str,
        "title": str,
        "title_fa": str,
        "commissions": t.Dict[str, float],
    },
)

CreateOrderResponse = t.TypedDict(
    "CreateOrderResponse",
    {
        "id": int,
        "market": MarketInfo,
        "amount1": str,
        "amount2": str,
        "price": str,
        "price_limit": str,
        "price_stop": OptionalStr,
        "price_limit_oco": OptionalStr,
        "type": str,
        "active_limit": str,
        "identifier": OptionalStr,
        "mode": str,
        "expected_gain": str,
        "expected_resource": str,
        "commission_percent": float,
        "user_share_percent": float,
        "expected_commission": str,
        "expected_user_gain": str,
        "expected_user_price": str,
        "gain_currency": CurrencyInfo,
        "resource_currency": CurrencyInfo,
        "fulfilled": float,
        "exchanged1": str,
        "exchanged2": str,
        "gain": str,
        "resource": str,
        "remain_amount": str,
        "average_price": str,
        "average_user_price": str,
        "commission": str,
        "user_commission": str,
        "user_gain": str,
        "created_at": str,
        "activated_at": str,
        "state": str,
        "req_to_cancel": bool,
        "info": t.Dict[str, t.Any],
        "closed_at": OptionalStr,
        "external_address": str,
    },
)

OpenOrdersResponse = t.TypedDict(
    "OpenOrdersResponse",
    {
        "count": int,
        "next": OptionalStr,
        "previous": OptionalStr,
        "results": t.List[CreateOrderResponse],
    },
)

CancelOrderResponse = t.TypedDict(
    "CancelOrderResponse",
    {
        "status": str,
        "id": str,
    },
)
