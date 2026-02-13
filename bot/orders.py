def place_market_order(client, symbol, side, quantity):
    return client.create_order(
        symbol=symbol.upper(),
        side=side.upper(),
        type="MARKET",
        quantity=quantity
    )


def place_limit_order(client, symbol, side, quantity, price):
    return client.create_order(
        symbol=symbol.upper(),
        side=side.upper(),
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )


def place_stop_market_order(client, symbol, side, quantity, stop_price):
    return client.create_order(
        symbol=symbol.upper(),
        side=side.upper(),
        type="STOP_MARKET",
        stopPrice=stop_price,
        quantity=quantity
    )


def format_response(response):
    return {
        "orderId": response.get("orderId"),
        "status": response.get("status"),
        "executedQty": response.get("executedQty"),
        "avgPrice": response.get("avgPrice", "N/A")
    }
