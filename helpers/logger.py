import logging

logger = logging.getLogger(__name__)

s_handler = logging.StreamHandler()
s_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")

s_handler.setFormatter(s_format)
logger.addHandler(s_handler)
logger.setLevel(logging.INFO)
