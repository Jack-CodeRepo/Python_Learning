#!/usr/bin/env python
# coding: utf-8
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

path_to_log="log/"
log_file_name="ngu_display_messages.log"

logging.basicConfig(filename=f"{path_to_log}{log_file_name}",
                    format='%(asctime)s :: %(message)s',
                    filemode='a')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

