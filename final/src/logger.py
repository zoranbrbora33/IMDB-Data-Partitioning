import logging
import sys
import os
import datetime as dt

logger = logging.getLogger('Logger')
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.addHandler(logging.FileHandler(os.path.join('../logs', dt.date.today().strftime('%Y-%m-%d.log'))))
logger.setLevel(logging.DEBUG)
