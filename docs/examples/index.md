# Examples

Here are some examples which help you to get started with the library.

## Initiate

Initiate client.

!!! note "Authentication"

    You can pass `api_key` and `api_secret` to client or set them as environment variables.

    When you pass them to client, they will override environment variables.

    If `api_key` and `api_secret` are provided, client will login automatically and get access and refresh tokens.

!!! tip "Environment variables are also supported."

    - :material-variable: `BITPIN_API_KEY` - API key.
    - :material-variable: `BITPIN_API_SECRET` - API secret.
    - :material-variable: `BITPIN_ACCESS_TOKEN` - Access token.
    - :material-variable: `BITPIN_REFRESH_TOKEN` - Refresh token.

??? code-ref "Reference"

    - Code Reference: [Client](../reference/clients)

=== "Sync"

    ```python title="client.py" linenums="1"
    from bitpin import Client

    client = Client("<API_KEY>", "<API_SECRET>")
    ```

=== "Async"

    ```python title="client.py" linenums="1"
    import asyncio
    from bitpin import AsyncClient

    client = AsyncClient("<API_KEY>", "<API_SECRET>")
    ```

### With Request Params

You can pass [requests](https://docs.python-requests.org/en/master/) OR [aiohttp](https://docs.aiohttp.org/en/stable/) params to client.

=== "Sync"

    ``` python title="with_request_params.py" linenums="1"
    from bitpin import Client

    client = Client("<API_KEY>", "<API_SECRET>", requests_params={
        "timeout": 10
    })
    ```

=== "Async"

    ``` python title="async_with_request_params.py" linenums="1"
    import asyncio
    from bitpin import AsyncClient

    client = AsyncClient("<API_KEY>", "<API_SECRET>", requests_params={
        "timeout": 10
    })
    ```

## Login

Login to get access and refresh tokens.

!!! warning

    Access token is valid for 15 minutes and refresh token is valid for 7 days.

??? code-ref "Reference"

    - Sync Code Reference: [Client.login](../reference/clients#src.bitpin.clients.client.Client.login)
    - Async Code Reference: [AsyncClient.login](../reference/clients#src.bitpin.clients.async_client.AsyncClient.login)
    - API Documentation Reference: [Login](https://docs.bitpin.ir/#02c24a5326)

=== "Sync"

    ```python title="login.py" linenums="1"
    from bitpin import Client

    client = Client("<API_KEY>", "<API_SECRET>")


    def main():
        login = client.login()
        print(login)


    if __name__ == "__main__":
        main()
    ```

=== "Async"

    ``` python title="login_async.py" linenums="1"
    import asyncio
    from bitpin import AsyncClient

    client = AsyncClient("<API_KEY>", "<API_SECRET>")


    async def main():
        login = await client.login()
        print(login)


    if __name__ == "__main__":
        asyncio.run(main())
    ```

```shell title="output" linenums="1"
{
    "refresh": "eyJ0eXAiOiJKV....kIjoyLCJpcCI6IjE3Mi4xOC4wLjEifQ.LJd44M3...-0CiH2gokd_OWGBN3UnI",
    "access": "eyJ0eXAiOiJKV1Q....JqdGkiOiI3ZmM0YWY2ZjY1N2Y0MDU5YWRlNTY3...iNjMxZSI8UpTDxOS_utTTZW36W0KgU"
}
```

## Refresh Token

Refresh access token.

??? code-ref "Reference"

    - Sync Code Reference: [Client.refresh_access_token](../reference/clients#src.bitpin.clients.client.Client.refresh_access_token)
    - Async Code Reference: [AsyncClient.refresh_access_token](../reference/clients#src.bitpin.clients.async_client.AsyncClient.refresh_access_token)
    - API Documentation Reference: [Refresh Token](https://docs.bitpin.ir/#9b81094f74)

=== "Sync"

    ```python title="refresh_access_token.py" linenums="1"
    from bitpin import Client

    client = Client("<API_KEY>", "<API_SECRET>")


    def main():
        refresh = client.refresh_access_token()
        print(refresh)


    if __name__ == "__main__":
        main()
    ```

=== "Async"

    ```python title="refresh_access_token_async.py" linenums="1"
    import asyncio
    from bitpin import AsyncClient

    client = AsyncClient("<API_KEY>", "<API_SECRET>")


    async def main():
        refresh = await client.refresh_access_token()
        print(refresh)


    if __name__ == "__main__":
        asyncio.run(main())
    ```

```shell title="output" linenums="1"
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI...mozL60Q6kK3j56MtYQy_95hEn6VQPDZw"
}
```

## Get User Info

Get user info.

??? code-ref "Reference"

    - Sync Code Reference: [Client.get_user_info](../reference/clients#src.bitpin.clients.client.Client.get_user_info)
    - Async Code Reference: [AsyncClient.get_user_info](../reference/clients#src.bitpin.clients.async_client.AsyncClient.get_user_info)
    - API Documentation Reference: [Get User Info](https://docs.bitpin.ir/#5b3c85d79e)

=== "Sync"

    ```python title="get_user_info.py" linenums="1"
    from bitpin import Client

    client = Client("<API_KEY>", "<API_SECRET>")


    def main():
        user_info = client.get_user_info()
        print(user_info)


    if __name__ == "__main__":
        main()
    ```

=== "Async"

    ```python title="get_user_info_async.py" linenums="1"
    import asyncio
    from bitpin import AsyncClient

    client = AsyncClient("<API_KEY>", "<API_SECRET>")


    async def main():
        user_info = await client.get_user_info()
        print(user_info)


    if __name__ == "__main__":
        asyncio.run(main())
    ```

```shell title="output" linenums="1"
{'user_identifier': 'XXXXXXXX', 'enable_limit_msg': True, 'enable_market_msg': True, 'enable_oco_msg': True, 'enable_stop_limit_msg': True, 'is_chart': False, 'is_classic': False, 'is_english_number': False, 'is_light': False, 'is_vertical': True, 'phone': '09123456789', 'todos': [], 'last_login_time': '2020-01-1T12:00:00.148151Z', 'state': 'accepted', 'is_phone_confirmed': True, 'is_email_confirmed': True, 'first_name': 'جان', 'last_name': 'دو', 'fullname': 'جان دو', 'birth_date_text': '1360-1-1', 'sex': 'man', 'home_phone': '', 'address': '', 'email': 'johndoe@gmail.com', 'two_factor_auth_enabled': True, 'two_factor_auth_type': 'email', 'level': {'id': 6, 'title': 'سطح ۶', 'required_score': 1000000000, 'order': 6, 'income_percent_per_transaction': 30, 'max_daily_withdraw': 800000000}, 'company_name': '', 'type': 'iranian', 'review_step': 1, 'accepted_step': 4, 'level_score': 1761017021, 'daily_withdraw': 0, 'daily_deposit': 0, 'monthly_withdraw': 0, 'remaining_daily_withdraw': 1000000, 'remaining_daily_deposit': 1000000000, 'remaining_monthly_withdraw': 30000000, 'announcement': None, 'accepted_step_4_temp': False, 'accepted_step_5_temp': False, 'tetherban': False}
```

## Get Currencies List

Get currencies list.

!!! warning
    :material-car-speed-limiter:{ .rateLimit } 10000/day or 200/minute if you are authenticated.

??? code-ref "Reference"

    - Sync Code Reference: [Client.get_currencies_list](../reference/clients#src.bitpin.clients.client.Client.get_currencies_info)
    - Async Code Reference: [AsyncClient.get_currencies_list](../reference/clients#src.bitpin.clients.async_client.AsyncClient.get_currencies_info)
    - API Documentation Reference: [Get Currencies List](https://docs.bitpin.ir/#7e59da3d0d)

=== "Sync"

    ```python title="get_currencies_list.py" linenums="1"
    from bitpin import Client

    client = Client()


    def main():
        currencies_list = client.get_currencies_info()
        print(currencies_list)


    if __name__ == "__main__":
        main()
    ```

=== "Async"

    ```python title="get_currencies_list_async.py" linenums="1"
    import asyncio
    from bitpin import AsyncClient

    client = AsyncClient()


    async def main():
        currencies_list = await client.get_currencies_info()
        print(currencies_list)


    if __name__ == "__main__":
        asyncio.run(main())
    ```

```shell title="output" linenums="1"
{'count': 120, 'next': None, 'previous': None, 'results': [{'id': 2, 'title': 'Toman', 'title_fa': 'تومان', 'code': 'IRT', 'image': 'https://cdn.bitpin.ir/media/market/currency/1610698086.png', 'min_withdraw': '12000', 'price_info': {}, 'price_info_usdt': {}, 'color': '00fd22', 'withdraw_commission': 0.0002, 'withdraw_commission_type': 'percent', 'max_withdraw_commission': '6000', 'tradable': True, 'for_test': False, 'decimal': 0, 'decimal_amount': 0, 'decimal_irt': 1, 'high_risk': False, 'show_high_risk': False}, {'id': 92, 'title': 'VeThor Token', 'title_fa': 'وتور', 'code': 'VTHO', 'image': 'https://cdn.bitpin.ir/media/market/currency/1634905227.svg', 'min_withdraw': '0', 'price_info': {'price': '0', 'time': '0', 'change': -0.0417, 'min': '0', 'max': '0', 'mean': '0', 'value': '0', 'amount': '0', 'market_value': '0', 'market_amount': '0'}, 'price_info_usdt': {'price': '0', 'time': '0', 'change': -0.044800000000000006, 'min': '0', 'max': '0', 'mean': '0', 'value': '0', 'amount': '0', 'market_value': '0', 'market_amount': '0'}, 'color': '7f81ba', 'withdraw_commission': '0', 'withdraw_commission_type': 'value', 'max_withdraw_commission': '0', 'tradable': True, 'for_test': False, 'decimal': 6, 'decimal_amount': 0, 'decimal_irt': 1, 'high_risk': False, 'show_high_risk': False}]}
```

## Get Markets Info

Get markets info.

!!! warning
    :material-car-speed-limiter:{ .rateLimit } 10000/day or 200/minute if you are authenticated.

??? code-ref "Reference"

    - Sync Code Reference: [Client.get_markets_info](../reference/clients#src.bitpin.clients.client.Client.get_markets_info)
    - Async Code Reference: [AsyncClient.get_markets_info](../reference/clients#src.bitpin.clients.async_client.AsyncClient.get_markets_info)
    - API Documentation Reference: [Get Markets Info](https://docs.bitpin.ir/#334792bb2b)

=== "Sync"

    ```python title="get_markets_info.py" linenums="1"
    from bitpin import Client

    client = Client()


    def main():
        markets_info = client.get_markets_info()
        print(markets_info)


    if __name__ == "__main__":
        main()
    ```

=== "Async"

    ```python title="get_markets_info_async.py" linenums="1"
    import asyncio
    from bitpin import AsyncClient

    client = AsyncClient()


    async def main():
        markets_info = await client.get_markets_info()
        print(markets_info)


    if __name__ == "__main__":
        asyncio.run(main())
    ```

```shell title="output" linenums="1"
{'count': 231, 'next': 'https://api.bitpin.ir/v1/mkt/markets/?page=2', 'previous': None, 'results': [{'id': 1, 'currency1': {'id': 1, 'title': 'Bitcoin', 'title_fa': 'بیت کوین', 'code': 'BTC', 'tradable': True, 'for_test': False, 'image': 'https://cdn.bitpin.ir/media/market/currency/1628415570.svg', 'decimal': 2, 'decimal_amount': 8, 'decimal_irt': 0, 'color': 'f7931a', 'high_risk': False, 'show_high_risk': False, 'withdraw_commission': '0.000550000000000000', 'tags': []}, 'currency2': {'id': 2, 'title': 'Toman', 'title_fa': 'تومان', 'code': 'IRT', 'tradable': True, 'for_test': False, 'image': 'https://cdn.bitpin.ir/media/market/currency/1610698086.png', 'decimal': 0, 'decimal_amount': 0, 'decimal_irt': 1, 'color': '00fd22', 'high_risk': False, 'show_high_risk': False, 'withdraw_commission': '0.000200000000000000', 'tags': []}, 'tradable': True, 'for_test': False, 'otc_sell_percent': '0.00800', 'otc_buy_percent': '0.00800', 'otc_max_buy_amount': '0.030000000000000000', 'otc_max_sell_amount': '0.030000000000000000', 'order_book_info': {'created_at': None, 'price': '1018041176', 'change': -0.0023, 'min': '975697937', 'max': '1024609580', 'time': '2022-03-08T13:54:52.000Z', 'mean': '1004787964', 'value': '10303509406', 'amount': '10.25013963'}, 'internal_price_info': {'created_at': 1646747693.366072, 'price': '1018041176', 'change': -0.2399, 'min': '975697937', 'max': '1028000000', 'time': None, 'mean': None, 'value': None, 'amount': None}, 'price_info': {'created_at': 1646747763.388, 'price': '1019566443', 'change': -0.05, 'min': '975067512', 'max': '1030178774', 'time': None, 'mean': None, 'value': None, 'amount': None}, 'price': '1019566443', 'title': 'Bitcoin/Toman', 'code': 'BTC_IRT', 'title_fa': 'بیت کوین/تومان', 'trading_view_source': 'BINANCE', 'otc_market': False}, {'id': 2, 'currency1': {'id': 1, 'title': 'Bitcoin', 'title_fa': 'بیت کوین', 'code': 'BTC', 'tradable': True, 'for_test': False, 'image': 'https://cdn.bitpin.ir/media/market/currency/1628415570.svg', 'decimal': 2, 'decimal_amount': 8, 'decimal_irt': 0, 'color': 'f7931a', 'high_risk': False, 'show_high_risk': False, 'withdraw_commission': '0.000550000000000000', 'tags': []}, 'currency2': {'id': 4, 'title': 'Tether', 'title_fa': 'تتر', 'code': 'USDT', 'tradable': True, 'for_test': False, 'image': 'https://cdn.bitpin.ir/media/market/currency/1628416117.svg', 'decimal': 1, 'decimal_amount': 2, 'decimal_irt': 0, 'color': '26a17b', 'high_risk': False, 'show_high_risk': False, 'withdraw_commission': '25.000000000000000000', 'tags': [{'name': 'استیبل کوین'}]}, 'tradable': True, 'for_test': False, 'otc_sell_percent': '0.00800', 'otc_buy_percent': '0.00800', 'otc_max_buy_amount': '0.033000000000000000', 'otc_max_sell_amount': '0.033000000000000000', 'order_book_info': {'created_at': None, 'price': '38815.88', 'change': -0.003, 'min': '37105.02', 'max': '39611.63', 'time': '2022-03-08T13:44:19.000Z', 'mean': '38461.02', 'value': '330372.37', 'amount': '8.57852165'}, 'internal_price_info': {'created_at': 1646747059.672099, 'price': '38815.88', 'change': -0.3099, 'min': '37105.02', 'max': '39611.63', 'time': None, 'mean': None, 'value': None, 'amount': None}, 'price_info': {'created_at': 1646747763.388, 'price': '38905.84', 'change': -0.2399, 'min': '37167.14', 'max': '39532.19', 'time': None, 'mean': None, 'value': None, 'amount': None}, 'price': '38905.84', 'title': 'Bitcoin/Tether', 'code': 'BTC_USDT', 'title_fa': 'بیت کوین/تتر', 'trading_view_source': 'BINANCE', 'otc_market': False}]}
```

## Get Wallets

Get wallets and balances.

!!! warning
    :material-car-speed-limiter:{ .rateLimit } 10000/day.

??? code-ref "Reference"

    - Sync Code Reference: [Client.get_wallets](../reference/clients#src.bitpin.clients.client.Client.get_wallets)
    - Async Code Reference: [AsyncClient.get_wallets](../reference/clients#src.bitpin.clients.async_client.AsyncClient.get_wallets)
    - API Documentation Reference: [Get Wallets](https://docs.bitpin.ir/#9b93495188)

=== "Sync"

    ```python title="get_wallets.py" linenums="1"
    from bitpin import Client

    client = Client("<API_KEY>", "<API_SECRET>")


    def main():
        wallets = client.get_wallets()
        print(wallets)


    if __name__ == "__main__":
        main()
    ```

=== "Async"

    ```python title="get_wallets_async.py" linenums="1"
    import asyncio
    from bitpin import AsyncClient

    client = AsyncClient("<API_KEY>", "<API_SECRET>")


    async def main():
        wallets = await client.get_wallets()
        print(wallets)


    if __name__ == "__main__":
        asyncio.run(main())
    ```

```shell title="output" linenums="1"
{'count': 112, 'next': None, 'previous': None, 'results': [{'id': 3108164, 'currency': {'id': 50, 'title': 'Harmony', 'title_fa': 'هارمونی', 'code': 'ONE', 'tradable': True, 'for_test': False, 'image': 'https://cdn.bitpin.ir/media/market/currency/1628418817.svg', 'decimal': 5, 'decimal_amount': 1, 'decimal_irt': 1, 'color': '56edc5', 'high_risk': False, 'show_high_risk': False, 'withdraw_commission': '0.000000000000000000', 'tags': []}, 'balance': '1671.6', 'frozen': '0.0', 'total': '1671.6', 'value': '5678468', 'value_frozen': '0', 'value_total': '5678468', 'usdt_value': '216.79', 'usdt_value_frozen': '0.00', 'usdt_value_total': '216.79', 'address': '', 'inviter_commission': '0.0', 'daily_withdraw': '0.0', 'remaining_daily_withdraw': '10000000.0'}, {'id': 3108166, 'currency': {'id': 47, 'title': 'Celer Network', 'title_fa': 'سلر نتورک', 'code': 'CELR', 'tradable': True, 'for_test': False, 'image': 'https://cdn.bitpin.ir/media/market/currency/1628418961.png', 'decimal': 5, 'decimal_amount': 1, 'decimal_irt': 1, 'color': 'e3e3e3', 'high_risk': False, 'show_high_risk': False, 'withdraw_commission': '0.000000000000000000', 'tags': []}, 'balance': '5631.6', 'frozen': '0.0', 'total': '5631.6', 'value': '5540368', 'value_frozen': '0', 'value_total': '5540368', 'usdt_value': '211.52', 'usdt_value_frozen': '0.00', 'usdt_value_total': '211.52', 'address': '', 'inviter_commission': '0.0', 'daily_withdraw': '0.0', 'remaining_daily_withdraw': '10000000.0'}]}
```

## Get Orderbook

Get orderbook.

??? code-ref "Reference"

    - Sync Code Reference: [Client.get_orderbook](../reference/clients#src.bitpin.clients.client.Client.get_orderbook)
    - Async Code Reference: [AsyncClient.get_orderbook](../reference/clients#src.bitpin.clients.async_client.AsyncClient.get_orderbook)
    - API Documentation Reference: [Get Orderbook](https://docs.bitpin.ir/#270b5bd78d)

=== "Sync"

    ```python title="get_orderbook.py" linenums="1"
    from bitpin import Client

    client = Client()


    def main():
        orderbook = client.get_orderbook(1, "buy")
        print(orderbook)


    if __name__ == "__main__":
        main()
    ```

=== "Async"

    ```python title="get_orderbook_async.py" linenums="1"
    import asyncio
    from bitpin import AsyncClient

    client = AsyncClient()


    async def main():
        orderbook = await client.get_orderbook(1, "buy")
        print(orderbook)


    if __name__ == "__main__":
        asyncio.run(main())
    ```

```shell title="output" linenums="1"
{'orders': [{'amount': '0.00793177', 'remain': '0.00340995', 'price': '1020020001', 'value': '3478225'}, {'amount': '0.04110803', 'remain': '0.03143967', 'price': '1020020000', 'value': '32069099'}, {'amount': '0.00437797', 'remain': '0.00437797', 'price': '1020000000', 'value': '4465528'}], 'volume': '93412.67506888'}
```

## Get Recent Trades

Get recent trades.

??? code-ref "Reference"

    - Sync Code Reference: [Client.get_recent_trades](../reference/clients#src.bitpin.clients.client.Client.get_recent_trades)
    - Async Code Reference: [AsyncClient.get_recent_trades](../reference/clients#src.bitpin.clients.async_client.AsyncClient.get_recent_trades)
    - API Documentation Reference: [Get Recent Trades](https://docs.bitpin.ir/#1dd63530b5)

=== "Sync"

    ```python title="get_recent_trades.py" linenums="1"
    from bitpin import Client

    client = Client()


    def main():
        recent_trades = client.get_recent_trades(1)
        print(recent_trades)


    if __name__ == "__main__":
        main()
    ```

=== "Async"

    ```python title="get_recent_trades_async.py" linenums="1"
    import asyncio
    from bitpin import AsyncClient

    client = AsyncClient()


    async def main():
        recent_trades = await client.get_recent_trades(1)
        print(recent_trades)


    if __name__ == "__main__":
        asyncio.run(main())
    ```

```shell title="output" linenums="1"
[{'time': 1647174307.768419, 'price': '1019000000', 'value': '11075213', 'match_amount': '0.01086870', 'type': 'sell', 'match_id': '73802972_73807087'}, {'time': 1647174307.656013, 'price': '1019000000', 'value': '5859993', 'match_amount': '0.00575072', 'type': 'sell', 'match_id': '73802711_73807087'}, {'time': 1647174307.605909, 'price': '1019000000', 'value': '18496580', 'match_amount': '0.01815169', 'type': 'sell', 'match_id': '73769110_73807087'}, {'time': 1647174307.547822, 'price': '1020000000', 'value': '4365538', 'match_amount': '0.00427993', 'type': 'sell', 'match_id': '73783129_73807087'}, {'time': 1647174307.497821, 'price': '1020020000', 'value': '883459', 'match_amount': '0.00086611', 'type': 'sell', 'match_id': '73800260_73807087'}]
```

## Get User Open Orders

Get user open orders.

!!! warning
    :material-car-speed-limiter:{ .rateLimit } 1000/hour.

??? code-ref "Reference"

    - Sync Code Reference: [Client.get_open_orders](../reference/clients#src.bitpin.clients.client.Client.get_open_orders)
    - Async Code Reference: [AsyncClient.get_open_orders](../reference/clients#src.bitpin.clients.async_client.AsyncClient.get_open_orders)
    - API Documentation Reference: [Get User Open Orders](https://docs.bitpin.ir/#8a7c2a2af5)

=== "Sync"

    ```python title="get_open_orders.py" linenums="1"
    from bitpin import Client

    client = Client("<API_KEY>", "<API_SECRET>")

    def main():
        open_orders = client.get_open_orders()
        print(open_orders)


    if __name__ == "__main__":
        main()
    ```

=== "Async"

    ```python title="get_open_orders_async.py" linenums="1"
    import asyncio
    from bitpin import AsyncClient

    client = AsyncClient("<API_KEY>", "<API_SECRET>")


    async def main():
        open_orders = await client.get_open_orders()
        print(open_orders)


    if __name__ == "__main__":
        asyncio.run(main())
    ```

```shell title="output" linenums="1"
{'count': 0, 'next': 'https://api.bitpin.ir/v1/odr/orders/?page=2', 'previous': None, 'results': [{'id': 230701011, 'market': {'id': 5, 'currency1': {'id': 4, 'title': 'Tether', 'title_fa': 'تتر', 'code': 'USDT', 'tradable': True, 'for_test': False, 'image': 'https://cdn.bitpin.ir/media/market/currency/1628416117.svg', 'decimal': 1, 'decimal_amount': 2, 'decimal_irt': 0, 'color': '26a17b', 'high_risk': False, 'show_high_risk': False, 'withdraw_commission': '25.000000000000000000', 'tags': [{'name': 'استیبل کوین'}]}, 'currency2': {'id': 2, 'title': 'Toman', 'title_fa': 'تومان', 'code': 'IRT', 'tradable': True, 'for_test': False, 'image': 'https://cdn.bitpin.ir/media/market/currency/1684671406.svg', 'decimal': 0, 'decimal_amount': 0, 'decimal_irt': 1, 'color': '00fd22', 'high_risk': False, 'show_high_risk': False, 'withdraw_commission': '0.000200000000000000', 'tags': []}, 'code': 'USDT_IRT', 'title': 'Tether/Toman', 'title_fa': 'تتر/تومان', 'commissions': {'sell': 0.0001, 'buy': 0.0002, 'taker': 0.0002, 'maker': 0.0001}}, 'amount1': '515.13', 'amount2': '25724046', 'price': '49937', 'price_limit': '49937', 'price_stop': None, 'price_limit_oco': None, 'type': 'sell', 'active_limit': '49937', 'identifier': None, 'mode': 'limit', 'expected_gain': '25724046', 'expected_resource': '515.13', 'commission_percent': 0.0001, 'user_share_percent': 0.9999, 'expected_commission': '2572', 'expected_user_gain': '25721473', 'expected_user_price': '49932', 'gain_currency': {'id': 2, 'title': 'Toman', 'title_fa': 'تومان', 'code': 'IRT', 'tradable': True, 'for_test': False, 'image': 'https://cdn.bitpin.ir/media/market/currency/1684671406.svg', 'decimal': 0, 'decimal_amount': 0, 'decimal_irt': 1, 'color': '00fd22', 'high_risk': False, 'show_high_risk': False, 'withdraw_commission': '0.000200000000000000', 'tags': []}, 'resource_currency': {'id': 4, 'title': 'Tether', 'title_fa': 'تتر', 'code': 'USDT', 'tradable': True, 'for_test': False, 'image': 'https://cdn.bitpin.ir/media/market/currency/1628416117.svg', 'decimal': 1, 'decimal_amount': 2, 'decimal_irt': 0, 'color': '26a17b', 'high_risk': False, 'show_high_risk': False, 'withdraw_commission': '25.000000000000000000', 'tags': [{'name': 'استیبل کوین'}]}, 'fulfilled': 0.61, 'exchanged1': '312.90', 'exchanged2': '15625405', 'gain': '15625405', 'resource': '312.90', 'remain_amount': '202.22', 'average_price': '49937', 'average_user_price': '49932', 'commission': '1562', 'user_commission': '1562', 'user_gain': '15623842', 'created_at': '2023-08-28T17:50:16.898905+03:30', 'activated_at': '2023-08-28T17:50:16.898610+03:30', 'state': 'active', 'req_to_cancel': False, 'info': {'otc_network': 0, 'send_to_order_book_task_id': 'cf554186-0511-4b5b-b067-3936d1a56ce7'}, 'closed_at': None, 'external_address': ''}]}
```

## Create Order

Create New Order.

!!! warning
    :material-car-speed-limiter:{ .rateLimit } 1000/hour.

??? code-ref "Reference"

    - Sync Code Reference: [Client.create_order](../reference/clients#src.bitpin.clients.client.Client.create_order)
    - Async Code Reference: [AsyncClient.create_order](../reference/clients#src.bitpin.clients.async_client.AsyncClient.create_order)
    - API Documentation Reference: [Create Order](https://docs.bitpin.ir/#34b353d77b)

=== "Sync"

    ```python title="create_order.py" linenums="1"
    from bitpin import Client

    client = Client("<API_KEY>", "<API_SECRET>")


    def main():
        order = client.create_order(
            market=5,
            type="buy",
            mode="limit",
            amount1=10,
            price=50000,
            price_limit=50000,
        )
        print(order)


    if __name__ == "__main__":
        main()
    ```

=== "Async"

    ```python title="create_order_async.py" linenums="1"

    import asyncio
    from bitpin import AsyncClient

    client = AsyncClient("<API_KEY>", "<API_SECRET>")


    async def main():
        order = await client.create_order(
            market=5,
            type="buy",
            mode="limit",
            amount1=10,
            price=50000,
            price_limit=50000,
        )
        print(order)


    if __name__ == "__main__":
        asyncio.run(main())
    ```

```shell title="output" linenums="1"
{'id': 230701370, 'market': {'id': 5, 'currency1': {'id': 4, 'title': 'Tether', 'title_fa': 'تتر', 'code': 'USDT', 'tradable': True, 'for_test': False, 'image': 'https://cdn.bitpin.ir/media/market/currency/1628416117.svg', 'decimal': 1, 'decimal_amount': 2, 'decimal_irt': 0, 'color': '26a17b', 'high_risk': False, 'show_high_risk': False, 'withdraw_commission': '25.000000000000000000', 'tags': [{'name': 'استیبل کوین'}]}, 'currency2': {'id': 2, 'title': 'Toman', 'title_fa': 'تومان', 'code': 'IRT', 'tradable': True, 'for_test': False, 'image': 'https://cdn.bitpin.ir/media/market/currency/1684671406.svg', 'decimal': 0, 'decimal_amount': 0, 'decimal_irt': 1, 'color': '00fd22', 'high_risk': False, 'show_high_risk': False, 'withdraw_commission': '0.000200000000000000', 'tags': []}, 'code': 'USDT_IRT', 'title': 'Tether/Toman', 'title_fa': 'تتر/تومان', 'commissions': {'sell': 0.0001, 'buy': 0.0002, 'taker': 0.0002, 'maker': 0.0001}}, 'amount1': '3.00', 'amount2': '148800', 'price': '49600', 'price_limit': '49600', 'price_stop': None, 'price_limit_oco': None, 'type': 'buy', 'active_limit': '49600', 'identifier': None, 'mode': 'limit', 'expected_gain': '3.00', 'expected_resource': '148800', 'commission_percent': 0.0001, 'user_share_percent': 0.9999, 'expected_commission': '0.00', 'expected_user_gain': '2.99', 'expected_user_price': '49604', 'gain_currency': {'id': 4, 'title': 'Tether', 'title_fa': 'تتر', 'code': 'USDT', 'tradable': True, 'for_test': False, 'image': 'https://cdn.bitpin.ir/media/market/currency/1628416117.svg', 'decimal': 1, 'decimal_amount': 2, 'decimal_irt': 0, 'color': '26a17b', 'high_risk': False, 'show_high_risk': False, 'withdraw_commission': '25.000000000000000000', 'tags': [{'name': 'استیبل کوین'}]}, 'resource_currency': {'id': 2, 'title': 'Toman', 'title_fa': 'تومان', 'code': 'IRT', 'tradable': True, 'for_test': False, 'image': 'https://cdn.bitpin.ir/media/market/currency/1684671406.svg', 'decimal': 0, 'decimal_amount': 0, 'decimal_irt': 1, 'color': '00fd22', 'high_risk': False, 'show_high_risk': False, 'withdraw_commission': '0.000200000000000000', 'tags': []}, 'fulfilled': 0.0, 'exchanged1': '0.00', 'exchanged2': '0', 'gain': '0.00', 'resource': '0', 'remain_amount': '3.00', 'average_price': '0', 'average_user_price': '0', 'commission': '0.00', 'user_commission': '0.00', 'user_gain': '0.00', 'created_at': '2023-08-28T17:51:57.333028+03:30', 'activated_at': '2023-08-28T17:51:57.332722+03:30', 'state': 'active', 'req_to_cancel': False, 'info': {'otc_network': 0, 'send_to_order_book_task_id': 'bc6a2856-d58b-492a-ac34-7161c6412350'}, 'closed_at': None, 'external_address': ''}
```

## Cancel Order

Cancel Order.

!!! warning
    :material-car-speed-limiter:{ .rateLimit } 1000/hour.

??? code-ref "Reference"

    - Sync Code Reference: [Client.cancel_order](../reference/clients#src.bitpin.clients.client.Client.cancel_order)
    - Async Code Reference: [AsyncClient.cancel_order](../reference/clients#src.bitpin.clients.async_client.AsyncClient.cancel_order)
    - API Documentation Reference: [Cancel Order](https://docs.bitpin.ir/#3fe8d57657)

=== "Sync"

    ```python title="cancel_order.py" linenums="1"
    from bitpin import Client

    client = Client("<API_KEY>", "<API_SECRET>")


    def main():
        order = client.cancel_order("230008812")
        print(order)


    if __name__ == "__main__":
        main()
    ```

=== "Async"

    ```python title="cancel_order_async.py" linenums="1"
    import asyncio
    from bitpin import AsyncClient

    client = AsyncClient("<API_KEY>", "<API_SECRET>")


    async def main():
        order = await client.cancel_order("230008812")
        print(order)


    if __name__ == "__main__":
        asyncio.run(main())
    ```

```shell title="output" linenums="1"
{'status': 'success', 'id': '230701370'}
```

## Get User Recent Trades

Get user recent trades.

!!! warning
    :material-car-speed-limiter:{ .rateLimit } 1000/hour.

??? code-ref "Reference"

    - Sync Code Reference: [Client.get_user_trades](../reference/clients#src.bitpin.clients.client.Client.get_user_trades)
    - Async Code Reference: [AsyncClient.get_user_trades](../reference/clients#src.bitpin.clients.async_client.AsyncClient.get_user_trades)
    - API Documentation Reference: [Get User Recent Trades](https://docs.bitpin.ir/#3fe8d57657)

=== "Sync"

    ```python title="get_user_trades.py" linenums="1"
    from bitpin import Client

    client = Client("<API_KEY>", "<API_SECRET>")


    def main():
        user_trades = client.get_user_trades()
        print(user_trades)


    if __name__ == "__main__":
        main()
    ```

=== "Async"

    ```python title="get_user_trades_async.py" linenums="1"
    import asyncio
    from bitpin import AsyncClient

    client = AsyncClient("<API_KEY>", "<API_SECRET>")


    async def main():
        user_trades = await client.get_user_trades()
        print(user_trades)


    if __name__ == "__main__":
        asyncio.run(main())
    ```

```shell title="output" linenums="1"
{'count': 1179, 'next': 'https://api.bitpin.ir/v1/odr/matches/?market=&type=&page=2', 'previous': None, 'results': [{'id': 3482, 'exchanged1': '1.00100000', 'exchanged2': '1001000000', 'price': '1000000000', 'market': {'id': 2, 'currency1': {'id': 1, 'title': 'btc', 'title_fa': 'btc', 'code': 'BTC', 'tradable': True, 'for_test': False, 'image': None, 'decimal': 1, 'decimal_amount': 6, 'decimal_irt': 1, 'color': '', 'high_risk': False, 'show_high_risk': False, 'withdraw_commission': '0.000000000000000000', 'tags': []}, 'currency2': {'id': 3, 'title': 'irt', 'title_fa': 'irt', 'code': 'IRT', 'tradable': True, 'for_test': False, 'image': None, 'decimal': 1, 'decimal_amount': 6, 'decimal_irt': 1, 'color': '', 'high_risk': False, 'show_high_risk': False, 'withdraw_commission': '0.000000000000000000', 'tags': []}, 'code': 'BTC_IRT', 'title': 'btc/irt', 'title_fa': 'btc/irt', 'commissions': {'sell': 0.0, 'buy': 0.0, 'taker': 0.0, 'maker': 0.0}}, 'created_at': '2022-04-10T14:20:01.574922+04:30', 'type': 'sell', 'commission': '0', 'user_type': 'sell', 'user_gain': '1001000000'}]}
```
