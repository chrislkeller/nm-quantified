#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
import datetime
import os
from os import listdir
from os.path import isfile, join
import logging
import pandas as pd

logger = logging.getLogger("root")
logging.basicConfig(
    format="\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG,
)


class CompileDailyCsvFiles(object):

    """
    This script is the second step to process
    the latest ABQ cannabis retail location
    approval data from its Cannabis Retail
    Location Approvals Map

    https://cabq.maps.arcgis.com/apps/dashboards/4be0b05fa6444888b7174e0d92c9747b
    """

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    dir_current = os.path.dirname(os.path.realpath(__file__))
    dir_data = "daily-data"
    path = os.path.join(dir_current, dir_data)

    def handle(self):
        files = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        for file in files:

            daily_output = []
            target = os.path.join(self.path, file)
            with open(target, encoding="utf-8") as f:
                raw_json = json.load(f)
                for item in raw_json:
                    _this = item["attributes"]
                    _this["date_data_acquired"] = file[:17]
                    _this["lat"] = item["geometry"]["x"]
                    _this["lon"] = item["geometry"]["y"]
                    _unix = _this["CreationDate"] / 1000
                    _this["creation_date_formal"] = datetime.datetime.utcfromtimestamp(
                        _unix
                    ).strftime("%Y-%m-%d")
                    daily_output.append(_this)
            latest_csv = "latest-nm-vaccine-counties.csv"
            self.write_csv(latest_csv, daily_output)

    def write_csv(self, file, data):
        file_saved = os.path.join(self.dir_current, self.dir_data, file)
        csv_data = pd.DataFrame(data)
        csv_data.to_csv(file_saved, encoding="utf-8", index=False)
        logger.debug("File saved to {0}".format(file_saved))


if __name__ == "__main__":
    task_run = CompileDailyCsvFiles()
    task_run.handle()
