#! /usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import os
import re
import logging
import datetime
import pandas as pd
import pytz
import altair as alt
import altair_latimes as lat

alt.themes.register('latimes', lat.theme)
alt.themes.enable('latimes')
alt.data_transformers.enable('default', max_rows=None)
# alt.renderers.enable('jupyterlab')
alt.renderers.enable('altair_viewer')

logger = logging.getLogger("root")
logging.basicConfig(
    format="\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG
)

class BuildingPermitRequest(object):

    path = '/Users/ckeller/_programming/_abq/_projects/_abq-building-permits'

    file = 'abq-building-permits.csv'

    pacific = pytz.timezone('US/Mountain')

    utc = pytz.UTC

    def get_data(self, *args, **kwargs):

        target_file = os.path.join(self.path, self.file)

        df = pd.read_csv(target_file, encoding='utf-8', sep='\t').sort_values(['IssueDate'])
        df['proper_date'] = df['IssueDate'].apply(self.toDate)
        df['proper_year'] = pd.DatetimeIndex(df['proper_date']).year
        df['proper_month'] = pd.DatetimeIndex(df['proper_date']).month
        df = df[(df['CommercialorResidential'] == 'Commercial')].reset_index()
        df.to_csv('analysis_file.csv')
        # chart = alt.Chart(df).mark_bar().encode(
        #     alt.X("proper_year:Q", bin=True),
        #     y=alt.Y('count():Q',),
        # ).interactive()
        # chart.show()

    def toDate(self, item):
        item = str(item)
        output = datetime.datetime(
            int(item[0:4]), int(item[4:6]), int(item[6:])
        )
        return output




if __name__ == '__main__':
    task_run = BuildingPermitRequest()
    task_run.get_data()
