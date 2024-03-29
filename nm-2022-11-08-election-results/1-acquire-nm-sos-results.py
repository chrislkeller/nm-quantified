#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import json
import datetime
import os
import logging

logger = logging.getLogger("root")
logging.basicConfig(
    format="\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG
)

"""
This script pulls down a json from the New Mexico
Secretary of State election results data for the
2022-11-08 general election
"""

timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")

dir_current = os.path.dirname(os.path.realpath(__file__))

dir_data = "results-csv"

file_output = '{0}-nm-sos-results.csv'.format(timestamp)

file_saved = os.path.join(dir_current, dir_data, file_output)

target_url = "https://electionresults.sos.state.nm.us/resultsCSV.aspx?text=All&type=STATE&map=CTY"

response = urllib.request.urlretrieve(target_url, file_saved)

logger.debug('File saved to {0}'.format(file_saved))
