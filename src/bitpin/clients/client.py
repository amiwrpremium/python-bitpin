"""# Bitpin Client."""

import requests

from .core import CoreClient
from .. import types as t
from .. import enums
from ..exceptions import APIException, RequestException


class Client(CoreClient):
    """
    Client.

    Methods:
        _init_session: Initialize session.
        _get: Make a GET request.
        _post: Make a POST request.
        _delete: Make a DELETE request.
        _request_api: Request API.
        _request: Request.
        _handle_response: Handle response.
        login: Login and set (refresh_token/access_token)
        refresh_access_token: Refresh token.
        get_user_info: Get user info.
        get_currencies_info: Get currencies info.
        get_markets_info: Get markets info.
        get_wallets: Get wallets.
        get_orderbook: Get orderbook.
        get_recent_trades: Get recent trades.
        get_open_orders: Get open orders.
        create_order: Create order.
        cancel_order: Cancel order.
        get_user_trades: Get user trades.
        close_connection: Close connection.

    Attributes:
        session (aiohttp.ClientSession): Session.
        api_key (str): API key.
        api_secret (str): API secret.
        refresh_token (str): Refresh token.
        access_token (str): Access token.
    """

    def _init_session(self) -> requests.Session:
        """
        Initialize session.

        Returns:
            session (aiohttp.ClientSession): Session.

        """

        session = requests.Session()
        session.headers["Content-Type"] = "application/json"
        session.headers["Accept"] = "application/json"
        return session

    def _get(  # type: ignore[no-untyped-def]
        self,
        path: str,
        signed: bool = False,
        version: str = CoreClient.PUBLIC_API_VERSION_1,
        **kwargs,
    ) -> t.DictStrAny:
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

        return self._request_api(enums.RequestMethod.GET, path, signed, version, **kwargs)

    def _post(  # type: ignore[no-untyped-def]
        self,
        path: str,
        signed: bool = False,
        version: str = CoreClient.PUBLIC_API_VERSION_1,
        **kwargs,
    ) -> t.DictStrAny:
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

        return self._request_api(enums.RequestMethod.POST, path, signed, version, **kwargs)

    def _delete(  # type: ignore[no-untyped-def]
        self,
        path: str,
        signed: bool = False,
        version: str = CoreClient.PUBLIC_API_VERSION_1,
        **kwargs,
    ) -> t.DictStrAny:
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

        return self._request_api(enums.RequestMethod.DELETE, path, signed, version, **kwargs)

    def _request_api(  # type: ignore[no-untyped-def]
        self,
        method: t.RequestMethods,
        path: str,
        signed: bool = False,
        version: str = CoreClient.PUBLIC_API_VERSION_1,
        **kwargs,
    ) -> t.DictStrAny:
        """
        Request API.

        Args:
            method (RequestMethod): Method.
            path (str): Path.
            signed (bool): Signed.
            version (str): Version.
            **kwargs: Kwargs.

        Returns:
            dict: Response.
        """

        uri = self._create_api_uri(path, version)
        return self._request(method, uri, signed, **kwargs)

    def _request(  # type: ignore[no-untyped-def]
        self, method: t.RequestMethods, uri: str, signed: bool, **kwargs
    ) -> t.DictStrAny:
        """
        Request.

        Args:
            method (RequestMethod): Method.
            uri (str): URI.
            signed (bool): Signed.
            **kwargs: Kwargs.

        Returns:
            dict: Response.
        """

        kwargs = self._get_request_kwargs(method, signed, **kwargs)

        with getattr(self.session, method)(uri, **kwargs) as response:
            self.response = response  # pylint: disable=attribute-defined-outside-init
            return self._handle_response(response)

    @staticmethod
    def _handle_response(response: requests.Response) -> t.DictStrAny:  # type: ignore[override]
        """
        Handle response.

        Args:
            response (aiohttp.ClientResponse): Response.

        Returns:
            dict: Response.

        Raises:
            APIException: API Exception.
            RequestException: Request Exception.
        """

        if not str(response.status_code).startswith("2"):
            if response.request.method.lower() == enums.RequestMethod.DELETE:  # type: ignore[union-attr]
                return {"status": "success", "id": response.request.path_url.split("/")[-2]}
            raise APIException(response, response.status_code, response.text)
        try:
            return response.json()  # type: ignore[no-any-return]
        except ValueError as exc:
            raise RequestException(f"Invalid Response: {response.text}") from exc

    def login(self, **kwargs) -> t.LoginResponse:  # type: ignore[no-untyped-def]
        """
        Login and set (refresh_token/access_token).

        Args:
            **kwargs: Kwargs.

        Returns:
            Response (LoginResponse): Response.

        References:
            [API Docs](https://docs.bitpin.ir/#02c24a5326)
        """

        kwargs["json"] = {"api_key": self.api_key, "secret_key": self.api_secret}
        _: t.LoginResponse = self._post(self.LOGIN_URL, **kwargs)  # type: ignore[assignment]

        self.refresh_token = _["refresh"]
        self.access_token = _["access"]

        return _

    def refresh_access_token(  # type: ignore[no-untyped-def]
        self, refresh_token: t.OptionalStr = None, **kwargs
    ) -> t.RefreshTokenResponse:
        """
        Refresh token.

        Args:
            refresh_token (str): Refresh token.
            **kwargs: Kwargs.

        Returns:
            Response (RefreshTokenResponse): Response.

        References:
            [API Docs](https://docs.bitpin.ir/#9b81094f74)
        """

        kwargs["json"] = {"refresh": refresh_token or self.refresh_token}
        _: t.RefreshTokenResponse = self._post(self.REFRESH_TOKEN_URL, **kwargs)  # type: ignore[assignment]

        self.access_token = _["access"]

        return _

    def get_user_info(self, **kwargs) -> t.DictStrAny:  # type: ignore[no-untyped-def]
        """
        Get user info.

        Args:
            **kwargs: Kwargs.

        Returns:
            Response (dict): Response.

        References:
            [API Docs](https://docs.bitpin.ir/#5b3c85d79e)
        """

        return self._get(self.USER_INFO_URL, signed=True, **kwargs)

    def get_currencies_info(self, page: int = 1, **kwargs) -> t.DictStrAny:  # type: ignore[no-untyped-def]
        """
        Get currencies info.

        Args:
            page (int): Page.
            **kwargs: Kwargs.

        Returns:
            Response (dict): Response.

        References:
            [API Docs](https://docs.bitpin.ir/#7e59da3d0d)

        Notes:
            Rate limit: 10000/day or 200/minute if you are authenticated.
        """

        return self._get(self.CURRENCIES_LIST_URL.format(page), **kwargs)

    def get_markets_info(self, page: int = 1, **kwargs) -> t.DictStrAny:  # type: ignore[no-untyped-def]
        """
        Get markets info.

        Args:
            page (int): Page.
            **kwargs: Kwargs.

        Returns:
            Response (dict): Response.

        References:
            [API Docs](https://docs.bitpin.ir/#334792bb2b)

        Notes:
            Rate limit: 10000/day or 200/minute if you are authenticated.
        """

        return self._get(self.MARKETS_LIST_URL.format(page), **kwargs)

    def get_wallets(self, **kwargs) -> t.DictStrAny:  # type: ignore[no-untyped-def]
        """
        Get wallets.

        Args:
            **kwargs: Kwargs.

        Returns:
            Response (dict): Response.

        References:
            [API Docs](https://docs.bitpin.ir/#9b93495188)

        Notes:
            Rate limit: 10000/day.
        """

        return self._get(self.WALLETS_URL, signed=True, **kwargs)

    def get_orderbook(  # type: ignore[no-untyped-def]
        self,
        market_id: int,
        type: t.OrderTypes,
        **kwargs,  # pylint: disable=redefined-builtin
    ) -> t.OrderbookResponse:
        """
        Get orderbook.

        Args:
            market_id (int): Market ID.
            type (OrderTypes): Type.
            **kwargs: Kwargs.

        Returns:
            Response (dict): Response.

        References:
            [API Docs](https://docs.bitpin.ir/#ec7180fc0e)
        """

        return self._get(self.ORDERBOOK_URL.format(market_id, str(type)), **kwargs)  # type: ignore[return-value]

    def get_recent_trades(self, market_id: int, **kwargs) -> t.TradeResponse:  # type: ignore[no-untyped-def]
        """
        Get recent trades.

        Args:
            market_id (int): Market ID.
            **kwargs: Kwargs.

        Returns:
            Response (dict): Response.

        References:
            [API Docs](https://docs.bitpin.ir/#1dd63530b5)
        """

        return self._get(self.RECENT_TRADES_URL.format(market_id), **kwargs)  # type: ignore[return-value]

    def get_open_orders(  # type: ignore[no-untyped-def]
        self,
        market_id: t.OptionalInt = None,
        type: t.OptionalOrderTypes = None,  # pylint: disable=redefined-builtin
        state: t.OptionalStr = None,
        mode: t.OptionalStr = None,
        identifier: t.OptionalStr = None,
        **kwargs,
    ) -> t.OpenOrdersResponse:
        """
        Get open orders.

        Args:
            market_id (int): Market ID.
            type (OrderTypes): Type.
            state (str): State.
            mode (str): Mode.
            identifier (str): Identifier.
            **kwargs: Kwargs.

        Returns:
            Response (dict): Response.

        References:
            [API Docs](https://docs.bitpin.ir/#8a7c2a2af5)
        """

        kwargs["params"] = {k: str(v) for k, v in locals().items() if v is not None and k not in ("self", "kwargs")}
        return self._get(self.ORDERS_URL, signed=True, **kwargs)  # type: ignore[return-value]

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
            mode (OrderModes): Mode.
            type (OrderTypes): Type.
            identifier (str): Identifier.
            price_limit (float): Price limit.
            price_stop (float): Price stop.
            price_limit_oco (float): Price limit oco.
            amount2 (float): Amount2.
            **kwargs: Kwargs.

        Returns:
            Response (dict): Response.

        References:
            [API Docs](https://docs.bitpin.ir/#34b353d77b)
        """

        kwargs["json"] = {k: str(v) for k, v in locals().items() if v is not None and k not in ("self", "kwargs")}
        return self._post(self.ORDERS_URL, signed=True, **kwargs)  # type: ignore[return-value]

    def cancel_order(self, order_id: str, **kwargs) -> t.CancelOrderResponse:  # type: ignore[no-untyped-def]
        """
        Cancel order.

        Args:
            order_id (str): Order ID.
            **kwargs: Kwargs.

        Returns:
            Response (dict): Response.

        References:
            [API Docs](https://docs.bitpin.ir/#3fe8d57657)
        """

        return self._delete(self.ORDERS_URL + f"{order_id}/", signed=True, **kwargs)  # type: ignore[return-value]

    def get_user_trades(  # type: ignore[no-untyped-def]
        self,
        market_id: t.OptionalInt = None,
        type: t.OptionalOrderTypes = None,  # pylint: disable=redefined-builtin
        **kwargs,
    ) -> t.DictStrAny:
        """
        Get user trades.

        Args:
            market_id (int): Market ID.
            type (OrderTypes): Type.
            **kwargs: Kwargs.

        Returns:
            Response (dict): Response.

        References:
            [API Docs](https://docs.bitpin.ir/#3fe8d57657)
        """

        kwargs["params"] = {k: str(v) for k, v in locals().items() if v is not None and k not in ("self", "kwargs")}
        return self._get(self.USER_TRADES_URL, signed=True, **kwargs)

    def close_connection(self) -> None:
        """Close connection."""

        self.session.close()
