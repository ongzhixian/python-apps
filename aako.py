# Python application to scrape for software news
################################################################################
# Import statements
################################################################################

import json
import logging
from datetime import datetime

################################################################################
# Setup logging configuration
################################################################################

logging_format = '%(asctime)-15s %(levelname)-8s %(message)s'
#logging_format = '%(asctime)-15s %(levelname)-8s %(module)-16s %(funcName)-24s %(message)s'
logging.basicConfig(filename='watch.log', level=logging.DEBUG, format=logging_format) # Log to file
console_logger = logging.StreamHandler() # Log to console as well
console_logger.setFormatter(logging.Formatter(logging_format))
logging.getLogger().addHandler(console_logger)

################################################################################
# Import helper modules
################################################################################

from helpers import *

################################################################################
# Setup appconfig
################################################################################

appconfig = app_helpers.appconfig

################################################################################
# Import api modules
################################################################################

#from api import *

################################################################################
# Import pages modules
################################################################################

#from pages import *

################################################################################
# Functions
################################################################################



################################################################################
# Main function
################################################################################

if __name__ == '__main__':
    logging.info("[PROGRAM START]")
    logging.critical("%8s test message %s" % ("CRITICAL", str(datetime.utcnow())))
    logging.error("%8s test message %s" % ("ERROR", str(datetime.utcnow())))
    logging.warning("%8s test message %s" % ("WARNING", str(datetime.utcnow())))
    logging.info("%8s test message %s" % ("INFO", str(datetime.utcnow())))
    logging.debug("%8s test message %s" % ("DEBUG", str(datetime.utcnow())))
    
    # # http://www.singaporepools.com.sg/en/product/sr/Pages/toto_results.aspx?sppl=RHJhd051bWJlcj0zNDQy
    # # http://www.singaporepools.com.sg/en/product/Pages/toto_results.aspx

    # # Scrape dates



# reference
# https://www.journaldev.com/18341/python-scikit-learn-tutorial
