import logging

def my_func():
    logger = logging.getLogger(__name__)
    logger.info("from imported module")
    logger.warning("from imported module")