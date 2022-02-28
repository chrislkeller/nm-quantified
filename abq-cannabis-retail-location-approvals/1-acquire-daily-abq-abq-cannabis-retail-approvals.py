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
This script pulls down the latest ABQ cannabis retail
location approval data from its Cannabis Retail
Location Approvals Map
"""

timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")

dir_current = os.path.dirname(os.path.realpath(__file__))

dir_data = "daily-data"

file_output = "{0}-abq-cannabis-retail-approvals.json".format(timestamp)

file_saved = os.path.join(dir_current, dir_data, file_output)

target_url = "https://services.arcgis.com/CWv1abTnC3urn4bV/ArcGIS/rest/services/Application_for_Cannabis_Retail_Location_Approval_ViewForPublicMap/FeatureServer/0/query?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=*&returnGeometry=true&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pjson&token="

response = urllib.request.urlopen(target_url)

raw = json.load(response)

with open(file_saved, "w", encoding="utf-8") as f:
    json.dump(raw["features"], f, ensure_ascii=False, indent=4)

logger.debug("File saved to {0}".format(file_saved))
