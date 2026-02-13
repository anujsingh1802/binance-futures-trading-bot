import os
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException
from .logging_config import logger

load_dotenv()

TESTNET_URL = "https://testnet.binancefuture.com"


class BinanceFuturesClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise ValueError("API keys not found. Check your .env file.")

        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = TESTNET_URL

        # Health check
        try:
            self.client.futures_ping()
            logger.info("Connected to Binance Futures Testnet successfully.")
        except Exception as e:
            logger.error(f"Connection failed: {str(e)}")
            raise

    def create_order(self, **kwargs):
        try:
            logger.info(f"ORDER_REQUEST | {kwargs}")
            response = self.client.futures_create_order(**kwargs)
            logger.info(f"ORDER_RESPONSE | {response}")
            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.message}")
            raise

        except Exception as e:
            logger.error(f"Unexpected Error: {str(e)}")
            raise
