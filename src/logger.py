import logging
import sys

# Configure logger
logger = logging.getLogger("katoolin3")
logger.setLevel(logging.INFO)

# Create console handler with formatting
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('[%(levelname)s] %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)

def setup_logger(debug: bool = False) -> None:
    if debug:
        logger.setLevel(logging.DEBUG)
        ch.setLevel(logging.DEBUG)
