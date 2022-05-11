import os
import time
import logging
BASE_PATH=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
LOG_PATH=os.path.join(BASE_PATH,"log")
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)

class Logger():
    def __init__(self):
        self.logname=os.path.join(LOG_PATH,"{}.log".format(time.strftime("%Y%m%d")))
        self.logger=logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        self.formater=logging.Formatter('[%(asctime)s][%(filename)s][%(lineno)d][%(levelname)s]:%(message)s')
        self.filelogger=logging.FileHandler(self.logname,mode = 'a',encoding = 'utf-8')
        self.filelogger.setLevel(logging.DEBUG)

        self.filelogger.setFormatter(self.formater)
        self.logger.addHandler(self.filelogger)

logger=Logger().logger