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
This script pulls down a copy of the bernalillo county
election results data in the 2021-11-02 election
"""

timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")

dir_current = os.path.dirname(os.path.realpath(__file__))

dir_json = "results-json"

file_output = '{0}-bernco-results.json'.format(timestamp)

file_saved = os.path.join(dir_current, dir_json, file_output)

target_url = "https://results.bernco.gov/electionResults.json?nocache={0}".format(timestamp.replace("-", ""))

logger.debug(target_url)

response = urllib.request.urlopen(target_url)

raw = json.load(response)

with open(file_saved, 'w', encoding='utf-8') as f:
    json.dump(raw, f, ensure_ascii=False, indent=4)

logger.debug('File saved to {0}'.format(file_saved))
