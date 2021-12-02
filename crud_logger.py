import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)
# create handler
rotating_h = logging.handlers.RotatingFileHandler('crud_log.log', maxBytes=2000, backupCount=10)
# setting level to handler
# rotating_h.setLevel(logging.NOTSET)

# formatter for handler
rotating_formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(pathname)s:%(filename)s:%(lineno)d:%(message)s',
                                       datefmt='%Y-%m-%dT%H:%M:%S')
# set formatter
rotating_h.setFormatter(rotating_formatter)
# add handler
logger.addHandler(rotating_h)
