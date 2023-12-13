"""# Core Client."""

import os
from abc import (
    ABC,
    abstractmethod,
)
from .. import types as t


class CoreClient(ABC):  # pylint: disable=too-many-instance-attributes
    """Core Client."""

    API_URL = "https://api.bitpin.ir"

    PUBLIC_API_VERSION_1 = "v1"
    PUBLIC_API_VERSION_2 = "v2"

    REQUEST_TIMEOUT: float = 10

    LOGIN_URL = "usr/api/login/"
    REFRESH_TOKEN_URL = "usr/refresh_token/"
    USER_INFO_URL = "usr/info/"
    CURRENCIES_LIST_URL = "mkt/currencies/?page={}"
    MARKETS_LIST_URL = "mkt/markets/?page={}"
    WALLETS_URL = "wlt/wallets/"
    ORDERBOOK_URL = "mth/actives/{}/?type={}"
    RECENT_TRADES_URL = "mth/matches/{}/"
    ORDERS_URL = "odr/orders/"
    USER_TRADES_URL = "odr/matches/?type={}"

    def __init__(  # type: ignore[no-untyped-def]
        self,
        api_key: t.OptionalStr = None,
        api_secret: t.OptionalStr = None,
        access_token: t.OptionalStr = None,
        refresh_token: t.OptionalStr = None,
        requests_params: t.OptionalDictStrAny = None,
        background_relogin: bool = False,
        background_relogin_interval: int = 60 * 60 * 24 * 6,
        background_refresh_token: bool = False,
        background_refresh_token_interval: int = 60 * 13,
    ):
        """
        Constructor.

        Args:
            api_key (str): API key.
            api_secret (str): API secret.
            access_token (str): Access token.
            refresh_token (str): Refresh token.
            requests_params (dict): Requests params.
            background_relogin (bool): Background refresh.
            background_relogin_interval (int): Background refresh interval.
            background_refresh_token (bool): Background refresh token.
            background_refresh_token_interval (int): Background refresh token interval.

        Notes:
            If `api_key` and `api_secret` are not provided, they will be read from the environment variables
            `BITPIN_API_KEY` and `BITPIN_API_SECRET` respectively.

            If `access_token` and `refresh_token` are not provided, they will be read from the environment variables
            `BITPIN_ACCESS_TOKEN` and `BITPIN_REFRESH_TOKEN` respectively.

            If `requests_params` are provided, they will be used as default for every request.

            If `requests_params` are provided in method's `kwargs`, they will override existing `requests_params`.

            If `background_relogin` is enabled, access token will be refreshed in background every
            `background_relogin_interval` seconds.

            If `background_refresh_token` is enabled, refresh token will be refreshed in background every
            `background_refresh_token_interval` seconds.
        """

        self.api_key = api_key or os.environ.get("BITPIN_API_KEY")
        self.api_secret = api_secret or os.environ.get("BITPIN_API_SECRET")
        self.access_token: t.OptionalStr = access_token or os.environ.get("BITPIN_ACCESS_TOKEN")
        self.refresh_token: t.OptionalStr = refresh_token or os.environ.get("BITPIN_REFRESH_TOKEN")

        self._background_relogin = background_relogin
        self._background_relogin_interval = background_relogin_interval
        self._background_refresh_token = background_refresh_token
        self._background_refresh_token_interval = background_refresh_token_interval

        self._requests_params = requests_params
        self.session = self._init_session()

    def _get_request_kwargs(self, method: t.RequestMethods, signed: bool, **kwargs) -> t.DictStrAny:  # type: ignore[no-untyped-def]
        kwargs["timeout"] = self.REQUEST_TIMEOUT

        if self._requests_params:
            kwargs.update(self._requests_params)

        data = kwargs.get("data", None)
        if data and isinstance(data, dict):
            kwargs["data"] = data

            if "requests_params" in kwargs["data"]:
                kwargs.update(kwargs["data"]["requests_params"])
                del kwargs["data"]["requests_params"]

        if signed is True:
            headers: t.DictStrAny = kwargs.get("headers", {})
            headers.update({"Authorization": f"Bearer {self.access_token}"})
            kwargs["headers"] = headers

        if data and method == "get":
            kwargs["params"] = "&".join(f"{data[0]}={data[1]}" for data in kwargs["data"])
            del kwargs["data"]

        return kwargs

    @staticmethod
    def _pick(response: t.DictStrAny, key: str, value: t.t.Any, result_key: str = "results") -> t.DictStrAny:
        for _ in response.get(result_key, []):
            if _[key] == value:
                response[result_key] = _
                return response
        raise ValueError(f"{key} {value} not found in {response}")

    def _create_api_uri(self, path: str, version: str = PUBLIC_API_VERSION_1) -> str:
        return self.API_URL + "/" + str(version) + "/" + path

    @abstractmethod
    def _init_session(self) -> t.HttpSession:
        """
        Initialize session.

        Returns:
            session (t.Union[requests.Session, aiohttp.ClientSession]): Session.
        """

        raise NotImplementedError

    @abstractmethod
    def _get(self, path: str, signed: bool = False, version: str = PUBLIC_API_VERSION_1, **kwargs) -> t.DictStrAny:  # type: ignore[no-untyped-def]
        """
        Make a GET request.

        Args:
            path (str): Path.
            signed (bool): Signed.
            version (str): Version.
            **kwargs: Kwargs.

        Returns:
            dict: Response.
        """

        raise NotImplementedError

    @abstractmethod
    def _post(self, path: str, signed: bool = False, version: str = PUBLIC_API_VERSION_1, **kwargs) -> t.DictStrAny:  # type: ignore[no-untyped-def]
        """
        Make a POST request.

        Args:
            path (str): Path.
            signed (bool): Signed.
            version (str): Version.
            **kwargs: Kwargs.

        Returns:
            dict: Response.
        """

        raise NotImplementedError

    @abstractmethod
    def _delete(self, path: str, signed: bool = False, version: str = PUBLIC_API_VERSION_1, **kwargs) -> t.DictStrAny:  # type: ignore[no-untyped-def]
        """
        Make a DELETE request.

        Args:
            path (str): Path.
            signed (bool): Signed.
            version (str): Version.
            **kwargs: Kwargs.

        Returns:
            dict: Response.
        """

        raise NotImplementedError

    @abstractmethod
    def _request_api(  # type: ignore[no-untyped-def]
        self,
        method: t.RequestMethods,
        path: str,
        signed: bool = False,
        version: str = PUBLIC_API_VERSION_1,
        **kwargs,
    ) -> t.DictStrAny:
        """
        Request API.

        Args:
            method (str): Method (GET, POST, PUT, DELETE).
            path (str): Path.
            signed (bool): Signed.
            version (str): Version.
            **kwargs: Kwargs.

        Returns:
            dict: Response.
        """

        raise NotImplementedError

    @abstractmethod
    def _request(self, method: t.RequestMethods, uri: str, signed: bool, **kwargs) -> t.DictStrAny:  # type: ignore[no-untyped-def]
        """
        Request.

        Args:
            method (str): Method (GET, POST, PUT, DELETE).
            uri (str): URI.
            signed (bool): Signed.
            **kwargs: Kwargs.

        Returns:
            dict: Response.
        """

        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def _handle_response(response: t.HttpResponses) -> t.DictStrAny:
        """
        Handle response.

        Args:
            response (t.Union[requests.Response, aiohttp.ClientResponse]): Response.

        Returns:
            dict: Response.
        """

        raise NotImplementedError

    @abstractmethod
    def _handle_login(self) -> None:
        """Handle login."""

        raise NotImplementedError

    @abstractmethod
    def _background_relogin_task(self) -> None:
        """Background relogin task."""

        raise NotImplementedError

    @abstractmethod
    def _background_refresh_token_task(self) -> None:
        """Background refresh token task."""

        raise NotImplementedError

    @abstractmethod
    def login(self, **kwargs) -> t.LoginResponse:  # type: ignore[no-untyped-def]
        """
        Login.

        Returns:
            dict: Response.
        """

        raise NotImplementedError

    @abstractmethod
    def refresh_access_token(self, refresh_token: t.OptionalStr = None, **kwargs) -> t.RefreshTokenResponse:  # type: ignore[no-untyped-def]
        """
        Refresh token.

        Args:
            refresh_token (str): Refresh token.

        Returns:
            dict: Response.
        """

        raise NotImplementedError

    @abstractmethod
    def get_user_info(self, **kwargs) -> t.DictStrAny:  # type: ignore[no-untyped-def]
        """
        Get user info.

        Returns:
            dict: Response.
        """

        raise NotImplementedError

    @abstractmethod
    def get_currencies_info(self, page: int = 1, **kwargs) -> t.DictStrAny:  # type: ignore[no-untyped-def]
        """
        Get currencies info.

        Args:
            page (int): Page.

        Returns:
            dict: Response.
        """

        raise NotImplementedError

    @abstractmethod
    def get_markets_info(self, page: int = 1, **kwargs) -> t.DictStrAny:  # type: ignore[no-untyped-def]
        """
        Get markets info.

        Args:
            page (int): Page.

        Returns:
            dict: Response.
        """

        raise NotImplementedError

    @abstractmethod
    def get_wallets(self, **kwargs) -> t.DictStrAny:  # type: ignore[no-untyped-def]
        """
        Get wallets.

        Returns:
            dict: Response.
        """

        raise NotImplementedError

    @abstractmethod
    def get_orderbook(self, market_id: int, type: t.OrderTypes, **kwargs) -> t.OrderbookResponse:  # type: ignore[no-untyped-def]  # pylint: disable=redefined-builtin
        """
        Get orderbook.

        Args:
            market_id (int): Market ID.
            type (str): Type.

        Returns:
            dict: Response.
        """

        raise NotImplementedError

    @abstractmethod
    def get_recent_trades(self, market_id: int, **kwargs) -> t.TradeResponse:  # type: ignore[no-untyped-def]
        """
        Get recent trades.

        Args:
            market_id (int): Market ID.

        Returns:
            dict: Response.
        """

        raise NotImplementedError

    @abstractmethod
    def get_user_orders(  # type: ignore[no-untyped-def]
        self,
        market_id: t.OptionalInt = None,
        type: t.OptionalOrderTypes = None,  # pylint: disable=redefined-builtin
        state: t.OptionalStr = None,
        mode: t.OptionalStr = None,
        identifier: t.OptionalStr = None,
        page: int = 1,
        **kwargs,
    ) -> t.OpenOrdersResponse:
        """
        Get user orders.

        Args:
            market_id (int): Market ID.
            type (str): Type.
            state (str): State.
            mode (str): Mode.
            identifier (str): Identifier.
            page (int): Page.

        Returns:
            dict: Response.
        """

        raise NotImplementedError

    @abstractmethod
    def create_order(  # type: ignore[no-untyped-def]
        self,
        market: int,
        amount1: float,
        price: float,
        mode: t.OrderModes,
        type: t.OrderTypes,  # pylint: disable=redefined-builtin
        identifier: t.OptionalStr = None,
        price_limit: t.OptionalFloat = None,
        price_stop: t.OptionalFloat = None,
        price_limit_oco: t.OptionalFloat = None,
        amount2: t.OptionalFloat = None,
        **kwargs,
    ) -> t.CreateOrderResponse:
        """
        Create order.

        Args:
            market (int): Market.
            amount1 (float): Amount1.
            price (float): Price.
            mode (str): Mode.
            type (str): Type.
            identifier (str): Identifier.
            price_limit (float): Price limit.
            price_stop (float): Price stop.
            price_limit_oco (float): Price limit oco.
            amount2 (float): Amount2.

        Returns:
            dict: Response.
        """

        raise NotImplementedError

    @abstractmethod
    def cancel_order(self, order_id: str, **kwargs) -> t.CancelOrderResponse:  # type: ignore[no-untyped-def]
        """
        Cancel order.

        Args:
            order_id (str): Order ID.

        Returns:
            dict: Response.
        """

        raise NotImplementedError

    @abstractmethod
    def get_user_trades(  # type: ignore[no-untyped-def]
        self,
        market_id: t.OptionalInt = None,
        type: t.OptionalOrderTypes = None,  # pylint: disable=redefined-builtin
        page: int = 1,
        **kwargs,
    ) -> t.DictStrAny:
        """
        Get user trades.

        Args:
            market_id (int): Market ID.
            type (str): Type.
            page (int): Page.

        Returns:
            dict: Response.
        """

        raise NotImplementedError

    @abstractmethod
    def close_connection(self) -> None:
        """Close connection."""

        raise NotImplementedError
