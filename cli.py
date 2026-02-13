import argparse
import sys
from bot.client import BinanceFuturesClient
from bot.orders import (
    place_market_order,
    place_limit_order,
    place_stop_market_order,
    format_response
)
from bot.validators import validate_input
from bot.logging_config import logger


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--qty", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_input(args.symbol, args.side, args.type, args.qty, args.price)

        client = BinanceFuturesClient()

        print("\n===== ORDER REQUEST =====")
        print(f"Symbol: {args.symbol.upper()}")
        print(f"Side: {args.side.upper()}")
        print(f"Type: {args.type.upper()}")
        print(f"Quantity: {args.qty}")
        if args.price:
            print(f"Price/Stop: {args.price}")
        print("=========================\n")

        order_type = args.type.upper()

        if order_type == "MARKET":
            response = place_market_order(client, args.symbol, args.side, args.qty)

        elif order_type == "LIMIT":
            response = place_limit_order(client, args.symbol, args.side, args.qty, args.price)

        elif order_type == "STOP_MARKET":
            response = place_stop_market_order(client, args.symbol, args.side, args.qty, args.price)

        else:
            raise ValueError("Invalid order type.")

        formatted = format_response(response)

        print("===== ORDER RESPONSE =====")
        print(f"Order ID: {formatted['orderId']}")
        print(f"Status: {formatted['status']}")
        print(f"Executed Quantity: {formatted['executedQty']}")
        print(f"Average Price: {formatted['avgPrice']}")
        print("==========================\n")

        print("✅ Order placed successfully")
        sys.exit(0)

    except Exception as e:
        logger.error(str(e))
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
