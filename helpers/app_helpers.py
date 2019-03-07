################################################################################
# Modules and functions import statements
################################################################################

import logging
import json

################################################################################
# Function decorators
################################################################################

################################################################################
# Basic functions
################################################################################

########################################
# Define core functions
########################################

def get_appconfig():
    logging.debug("Opening app_config.json")
    appconfig_file = open( 'app_config.json' )
    logging.debug("Loading app_config.json")
    appconfig = json.load( appconfig_file )
    logging.debug("app_config loaded")
    return appconfig

def get_hostname():
    import socket
    hostname = socket.gethostname()
    return hostname


################################################################################
# Variables dependent on Application basic functions
################################################################################

appconfig = get_appconfig()
hostname = get_hostname()

################################################################################
# Main function
################################################################################

if __name__ == '__main__':
    pass
