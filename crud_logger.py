import logging
import os
from logging.handlers import RotatingFileHandler
from constants.constants import MB_TO_BYTE
import config.config


def mb_to_byte_method(file_size_in_mb):
    """
    This Method convert MB to bytes
    """
    bytes = file_size_in_mb * MB_TO_BYTE
    # print('bytes:', bytes)
    return bytes


logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)
# Get environment variables
file_size_in_mb = int(os.getenv('FILE_SIZE'))
# create handler
rotating_h = logging.handlers.RotatingFileHandler('crud_log.log', maxBytes=mb_to_byte_method(file_size_in_mb),
                                                  backupCount=100)
# setting level to handler
# rotating_h.setLevel(logging.NOTSET)

# formatter for handler
rotating_formatter = logging.Formatter(
    '%(asctime)s :   Logger Level- %(levelname)s   :    Path- %(pathname)s    :   File Name - %(filename)s    :   Line No- %(lineno)d  :   message-     %(message)s',
    datefmt='Date- %Y-%m-%d Time- %H:%M:%S')
# set formatter
rotating_h.setFormatter(rotating_formatter)
# add handler
logger.addHandler(rotating_h)
