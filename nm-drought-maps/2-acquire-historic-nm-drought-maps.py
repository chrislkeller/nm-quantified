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

start_date = datetime.datetime(2021, 6, 8)

dir_current = os.path.dirname(os.path.realpath(__file__))

dir_maps = "weekly-maps"

while start_date.year <= 2021:

    timestamp = start_date.strftime("%Y%m%d")

    base_url = "https://droughtmonitor.unl.edu/data/png/"

    url_variable = '{0}/{0}'.format(timestamp, timestamp)

    # url_suffix = "_nm_date.png"

    url_suffix = "_nm_cat.png"

    target_url = '{0}{1}{2}'.format(base_url, url_variable, url_suffix)

    file_output = '{0}{1}'.format(timestamp, url_suffix)

    file_saved = os.path.join(dir_current, dir_maps, file_output)

    response = urllib.request.urlretrieve(target_url, file_saved)

    logger.debug('File saved to {0}'.format(file_saved))

    start_date = start_date - timedelta(days=7)

    logging.debug("Preparing to download the next map")
