# -*- coding: utf-8 -*-
# ==================================================================================================

# source: https://www.geeksforgeeks.org/logging-in-python/

# ==================================================================================================
#   IMPORT
# ==================================================================================================

import logging

from logging.handlers import RotatingFileHandler

# ==================================================================================================
#   FONCTIONS
# ==================================================================================================

logging.basicConfig(filename="log/ngu_display_messages.log",
                    format='%(asctime)s :: %(message)s',
                    filemode='a')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

