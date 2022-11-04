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
    level=logging.DEBUG,
)

"""
This script pulls down daily snapshots of monthly sales data
displayed on New Mexico's Cannabis Reporting Online Portal.

https://qimw5q0w5j.execute-api.us-west-2.amazonaws.com/prod/default.html

State caveats:

All information shared via the C.R.O..P are public documents reported by the State’s track and trace system. The Cannabis Control Division does not guarantee completeness, accuracy, timeliness, or the results obtained from the use of this information, or offers a warranty of any kind, express or implied, but not limited to warranties of performance, merchantability, and fitness for a particular purpose.

The CCD attempts to ensure that the C.R.O.P is complete and accurate, however, because data are self-reported by licensees, they might contain typographical errors, sales or product errors, or other inaccuracies.

Further, the CCD assumes no responsibility for licensees’ errors and reserves the right to: (i) add, edit, or remove reported data; (ii) correct any errors, inaccuracies, or omissions; and (iii) make changes to sales figures, product, or any other information provided.
"""

timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")

dir_current = os.path.dirname(os.path.realpath(__file__))

dir_json = "topline/json"

file_output = "{0}-nm-daily-topline.json".format(timestamp)

file_saved = os.path.join(dir_current, dir_json, file_output)

target_url = "https://qimw5q0w5j.execute-api.us-west-2.amazonaws.com/prod/GetTotalsYTD"

response = urllib.request.urlopen(target_url)

raw = json.load(response)

with open(file_saved, "w", encoding="utf-8") as f:
    json.dump(raw["data"], f, ensure_ascii=False, indent=4)

logger.debug("File saved to {0}".format(file_saved))
