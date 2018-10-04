import sub
import logging
import uuid

CONTAINER_ID = str(uuid.uuid4())

'''
Add container id to logs
'''
LOG_FORMAT = "%(levelname)s:%(name)s:{container_id}:%(message)s" 
logging.basicConfig(
    format=LOG_FORMAT.format(container_id=CONTAINER_ID)
    )
logger = logging.getLogger(__name__)

logger.info("this is an informative message")
logger.warning("this is an informative message")
sub.my_func()

logging.getLogger().setLevel(logging.DEBUG)
logger.info("this is an informative message")
logger.warning("this is an informative message")
sub.my_func()
