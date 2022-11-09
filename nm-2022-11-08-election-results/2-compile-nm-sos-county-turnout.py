#! /usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from distutils.log import debug
import os
from os import listdir
from os.path import isfile, join
import json
import logging
import pandas as pd

logger = logging.getLogger("root")
logging.basicConfig(
    format="\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG
)


class BuildLatestCsv(object):

    """
    This script creates a csv from the latest json file
    of county by county turnout from the New Mexico
    Secretary of State for the 2022-11-08 general election
    """

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    dir_current = os.path.dirname(os.path.realpath(__file__))
    dir_data = "turnout-json"
    path = os.path.join(dir_current, dir_data)

    def handle(self):
        latest_output = []

        # get a list of files
        files = [os.path.join(self.path, f) for f in listdir(self.path) if isfile(join(self.path, f))]
        target = max(files, key=os.path.getctime)
        with open(target, encoding='utf-8') as f:
            raw_json = json.load(f)
            for item in raw_json:
                item['acquired_datestamp'] = self.timestamp
                latest_output.append(item)
        latest_csv = "latest-nm-sos-turnout.csv"

        # write the data to a file
        self.write_csv(latest_csv, latest_output)

    def write_csv(self, file, data):
        file_saved = os.path.join(self.dir_current, file)
        csv_data = pd.DataFrame(data)
        csv_data.to_csv(file_saved, encoding='utf-8', index=False)
        logger.debug('File saved to {0}'.format(file_saved))


if __name__ == '__main__':
    task_run = BuildLatestCsv()
    task_run.handle()
