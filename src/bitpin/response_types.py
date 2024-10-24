"""
# Types.

Types for Python Bitpin.

## Description
This file contains all the types used in the project.
"""

import asyncio
import typing as t
from datetime import datetime

import aiohttp
import requests

from . import enums

# General Types:
OptionalStr = t.Optional[str]
OptionalInt = t.Optional[int]
OptionalFloat = t.Optional[float]
OptionalStrList = t.Optional[list[str]]
OptionalDate = t.Optional[datetime]

DictStrAny = dict[str, t.Any]
OptionalDictStrAny = t.Optional[DictStrAny]

EventLoop = asyncio.AbstractEventLoop
OptionalEventLoop = t.Optional[EventLoop]

# Client Types:
OrderTypeBuy = t.Literal["buy"]
OrderTypeSell = t.Literal["sell"]
OrderTypes = t.Union[OrderTypeBuy, OrderTypeSell, enums.OrderType]

OptionalOrderTypes = t.Optional[OrderTypes]
OptionalOrderTypesList = t.Optional[list[OrderTypes]]

OrderStateInitial = t.Literal["initial"]
OrderStateActive = t.Literal["active"]
OrderStateClosed = t.Literal["closed"]
OrderState = t.Union[OrderStateInitial, OrderStateActive, OrderStateClosed, enums.OrderState]
OptionalOrderState = t.Optional[OrderState]
OptionalOrderStateList = t.Optional[list[OrderState]]

QuoteAssetIRT = t.Literal["IRT"]
QuoteAssetUSDT = t.Literal["USDT"]
OrderbookQuoteAsset = t.Union[QuoteAssetIRT, QuoteAssetUSDT, enums.OrderBookQuoteAsset]
OptionalQuoteAsset = t.Optional[OrderbookQuoteAsset]

OrderModeLimit = t.Literal["limit"]
OrderModeMarket = t.Literal["market"]
OrderModeOCO = t.Literal["oco"]
OrderModeStopLimit = t.Literal["stop_limit"]
OrderModes = t.Union[OrderModeLimit, OrderModeMarket, OrderModeOCO, OrderModeStopLimit, enums.OrderMode]
OptionalOrderModes = t.Optional[OrderModes]
OptionalOrderModesList = t.Optional[list[OrderModes]]

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


# Request Types:
class OrderDict(t.TypedDict):
    symbol: str
    base_amount: float
    price: float
    side: OrderTypes
    type: OrderModes


BulkOrderList = list[OrderDict]

# Response Types:
CurrenciesInfo = list[
    t.TypedDict(
        "CurrenciesInfo",
        {"currency": str, "name": str, "tradable": bool, "precision": str},
    )
]

MarketsInfo = list[
    t.TypedDict(
        "MarketsInfo",
        {
            "symbol": str,
            "name": str,
            "base": str,
            "quote": str,
            "tradable": bool,
            "price_precision": str,
            "base_amount_precision": str,
            "quote_amount_precision": str,
        },
    )
]

TickersInfo = list[
    t.TypedDict(
        "TickersInfo",
        {
            "symbol": str,
            "price": str,
            "daily_change_price": float,
            "low": str,
            "high": str,
            "timestamp": float,
        },
    )
]

RecentTradesInfo = list[
    t.TypedDict(
        "RecentTradesInfo",
        {
            "id": str,
            "price": str,
            "base_amount": str,
            "quote_amount": str,
            "side": OrderTypes,
        },
    )
]


class InnerOrderbookResponse(t.TypedDict):
    price: str
    quantity: str


class OrderbookResponse(t.TypedDict):
    asks: list[InnerOrderbookResponse]
    bids: list[InnerOrderbookResponse]


class LoginResponse(t.TypedDict):
    refresh: str
    access: str


class RefreshTokenResponse(t.TypedDict):
    access: str


WalletInfo = list[
    t.TypedDict(
        "WalletInfo",
        {"id": int, "asset": str, "balance": str, "frozen": str, "service": str},
    )
]


class CreateOrderResponse(t.TypedDict):
    id: int
    symbol: str
    type: OrderModes
    side: OrderTypes
    price: str
    stop_price: OptionalStr
    oco_target_price: OptionalStr
    base_amount: str
    quote_amount: str
    identifier: OptionalStr
    state: str
    closed_at: OptionalStr
    created_at: str
    dealed_base_amount: str
    dealed_quote_amount: str
    req_to_cancel: bool
    commission: str


OpenOrdersResponse = list[
    t.TypedDict(
        "OpenOrdersResponse",
        {
            "id": int,
            "symbol": str,
            "type": OrderModes,
            "side": OrderTypes,
            "base_amount": str,
            "quote_amount": str,
            "price": str,
            "stop_price": OptionalStr,
            "oco_target_price": OptionalStr,
            "identifier": OptionalStr,
            "state": str,
            "created_at": str,
            "closed_at": OptionalStr,
            "dealed_base_amount": str,
            "dealed_quote_amount": str,
            "req_to_cancel": bool,
            "commission": str,
        },
    )
]

TradeResponse = list[
    t.TypedDict(
        "TradeResponse",
        {
            "id": int,
            "symbol": str,
            "base_amount": str,
            "quote_amount": str,
            "price": str,
            "created_at": str,
            "commission": str,
            "side": OrderTypes,
            "order_id": int,
            "identifier": OptionalStr,
        },
    )
]


class CancelOrderResponse(t.TypedDict):
    status: str
    id: str


CancelBulkOrderResponse = list[
    t.TypedDict(
        "CancelBulkOrderResponse",
        {
            "canceled_orders": list[OptionalStr],
            "not_canceled_orders": list[OptionalStr],
        },
    )
]
