"""
# Deprecated Types.

Types for Python Bitpin.

## Description
This file contains all the types used in the project.
"""

import asyncio
import typing as t

import aiohttp
import requests

from . import deprecated_enums

# General Types:
OptionalStr = t.Optional[str]
OptionalInt = t.Optional[int]
OptionalFloat = t.Optional[float]

DictStrAny = dict[str, t.Any]
OptionalDictStrAny = t.Optional[DictStrAny]

EventLoop = asyncio.AbstractEventLoop
OptionalEventLoop = t.Optional[EventLoop]

# Client Types:
OrderTypeBuy = t.Literal["buy"]
OrderTypeSell = t.Literal["sell"]
OrderTypes = t.Union[OrderTypeBuy, OrderTypeSell, deprecated_enums.OrderType]
OptionalOrderTypes = t.Optional[OrderTypes]

OrderModeLimit = t.Literal["limit"]
OrderModeMarket = t.Literal["market"]
OrderModeOCO = t.Literal["oco"]
OrderModeStopLimit = t.Literal["stop_limit"]
OrderModes = t.Union[
    OrderModeLimit,
    OrderModeMarket,
    OrderModeOCO,
    OrderModeStopLimit,
    deprecated_enums.OrderMode,
]
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
    deprecated_enums.RequestMethod,
]


# Response Types:
class ResultListResponse(t.TypedDict):
    count: int | None
    next: str | None
    previous: str | None
    results: list[DictStrAny]


class InnerOrderbookResponse(t.TypedDict):
    amount: str
    price: str
    remain: str
    value: str


class OrderbookResponse(t.TypedDict):
    orders: list[InnerOrderbookResponse]
    volume: str


class InnerTradeResponse(t.TypedDict):
    time: float
    price: str
    value: str
    match_amount: str
    type: str
    match_id: str


TradeResponse = list[InnerTradeResponse]


class LoginResponse(t.TypedDict):
    refresh: str
    access: str


class RefreshTokenResponse(t.TypedDict):
    access: str


class CurrencyInfo(t.TypedDict):
    id: int
    title: str
    title_fa: str
    code: str
    tradable: bool
    for_test: bool
    image: str
    decimal: int
    decimal_amount: int
    decimal_irt: int
    color: str
    high_risk: bool
    show_high_risk: bool
    withdraw_commission: str
    tags: list[DictStrAny]


class WalletInfo(t.TypedDict):
    id: int
    currency: CurrencyInfo
    balance: str
    frozen: str
    total: str
    value: str
    value_frozen: str
    value_total: str
    usdt_value: str
    usdt_value_frozen: str
    usdt_value_total: str
    address: str
    inviter_commission: str
    service: str
    daily_withdraw: str


class MarketInfo(t.TypedDict):
    id: int
    currency1: CurrencyInfo
    currency2: CurrencyInfo
    code: str
    title: str
    title_fa: str
    commissions: dict[str, float]


class CreateOrderResponse(t.TypedDict):
    id: int
    market: MarketInfo
    amount1: str
    amount2: str
    price: str
    price_limit: str
    price_stop: OptionalStr
    price_limit_oco: OptionalStr
    type: str
    active_limit: str
    identifier: OptionalStr
    mode: str
    expected_gain: str
    expected_resource: str
    commission_percent: float
    user_share_percent: float
    expected_commission: str
    expected_user_gain: str
    expected_user_price: str
    gain_currency: CurrencyInfo
    resource_currency: CurrencyInfo
    fulfilled: float
    exchanged1: str
    exchanged2: str
    gain: str
    resource: str
    remain_amount: str
    average_price: str
    average_user_price: str
    commission: str
    user_commission: str
    user_gain: str
    created_at: str
    activated_at: str
    state: str
    req_to_cancel: bool
    info: dict[str, t.Any]
    closed_at: OptionalStr
    external_address: str


class OpenOrdersResponse(t.TypedDict):
    count: int
    next: OptionalStr
    previous: OptionalStr
    results: list[CreateOrderResponse]


class CancelOrderResponse(t.TypedDict):
    status: str
    id: str
