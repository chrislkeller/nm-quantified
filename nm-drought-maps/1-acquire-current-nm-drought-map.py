#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import json
import datetime
from datetime import timedelta
import os
import logging

logger = logging.getLogger("root")
logging.basicConfig(
    format="\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG
)

"""
This script pulls down the weekly New Mexico drought map
issued each week by the U.S. Drought Monitor
"""

suffixes = [
    '_nm_date.png',
    '_nm_cat.png',
]

timestamp = datetime.datetime.now().strftime("%Y%m%d")

dir_current = os.path.dirname(os.path.realpath(__file__))

dir_maps = "weekly-maps"

base_url = "https://droughtmonitor.unl.edu/data/png/"

url_variable = 'current/current'

for url_suffix in suffixes:
    target_url = '{0}{1}{2}'.format(base_url, url_variable, url_suffix)

    file_output = '{0}{1}'.format(timestamp, url_suffix)

    file_saved = os.path.join(dir_current, dir_maps, file_output)

    response = urllib.request.urlretrieve(target_url, file_saved)

    logger.debug('File saved to {0}'.format(file_saved))
