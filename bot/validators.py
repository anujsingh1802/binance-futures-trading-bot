VALID_SIDES = ["BUY", "SELL"]
VALID_TYPES = ["MARKET", "LIMIT", "STOP_MARKET"]


def validate_input(symbol, side, order_type, quantity, price):
    symbol = symbol.upper()
    side = side.upper()
    order_type = order_type.upper()

    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT-M symbols allowed (e.g., BTCUSDT).")

    if side not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL.")

    if order_type not in VALID_TYPES:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP_MARKET.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price required for LIMIT order.")

    if order_type == "STOP_MARKET" and price is None:
        raise ValueError("Stop price required for STOP_MARKET order.")
