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
This script pulls down the weekly New Mexico crop
progress report issued by the U.S. Department of Agriculture
"""

timestamp = datetime.datetime.now().strftime("%Y-%m-%d")

dir_current = os.path.dirname(os.path.realpath(__file__))

dir_pdfs = "weekly-reports"

file_output = '{0}-nm-crop-outlook.pdf'.format(timestamp)

file_saved = os.path.join(dir_current, dir_pdfs, file_output)

target_url = "https://www.nass.usda.gov/Statistics_by_State/New_Mexico/Publications/Crop_Progress_&_Condition/2021/current_nm.pdf"

response = urllib.request.urlretrieve(target_url, file_saved)

logger.debug('File saved to {0}'.format(file_saved))
