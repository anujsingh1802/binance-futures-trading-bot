import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "trading.log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logger = logging.getLogger("trading_bot")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(
    logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
)

logger.addHandler(file_handler)
