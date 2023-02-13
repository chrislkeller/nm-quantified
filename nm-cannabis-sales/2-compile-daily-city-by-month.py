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
    This script is the second step to process daily
    snapshots of total sales data by city displayed
    on New Mexico's cannabis reporting online portal.

    For each json file in the daily-json directory
    it makes a corresponding csv file with the same
    date and time prefix daily-data directory.
    """

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    dir_current = os.path.dirname(os.path.realpath(__file__))
    dir_json = "city-level/json"
    dir_csv = "city-level/csv"
    path = os.path.join(dir_current, dir_json)
    texas_towns = [
        "Anthony",
        "Carlsbad",
        "Chaparral",
        "Clayton",
        "Clovis",
        "Hobbs",
        "Las Cruces",
        "Logan",
        "Lovington",
        "Mesilla",
        "Portales",
        "Roswell",
        "Sunland Park",
        "Texico",
    ]

    def handle(self):
        files = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        for file in files:
            if not file.startswith("."):
                if file[-12:] == "monthly.json":
                    daily_output = []
                    target = os.path.join(self.path, file)
                    with open(target, encoding="utf-8") as f:
                        raw_json = json.load(f)
                        for item in raw_json:
                            item["City"] = item["City"].title()
                            if item["City"] in self.texas_towns:
                                item["border"] = "Texas"
                            item["acquired_datestamp"] = file[:17]
                            daily_output.append(item)
                    daily_csv = "{0}-nm-daily-city-monthly.csv".format(file[:17])
                    self.write_csv(daily_csv, daily_output)

    def write_csv(self, file, data):
        file_saved = os.path.join(self.dir_current, self.dir_csv, file)
        if os.path.isfile(file_saved):
            logger.debug("File already exists at {0}".format(file_saved))
        else:
            csv_data = pd.DataFrame(data)
            csv_data.to_csv(file_saved, encoding="utf-8", index=False)
            logger.debug("File saved to {0}".format(file_saved))


if __name__ == "__main__":
    task_run = CompileDailyCsvFiles()
    task_run.handle()
