abq_cannabis_retail_approvals.db:
	geojson-to-sqlite abq_cannabis_retail_approvals.db latest_cannabis_retail_approvals daily-data/latest-abq-cannabis-retail-approvals.geojson --spatial-index --pk=globalid

	geojson-to-sqlite abq_cannabis_retail_approvals.db abq_city_council_districts gis_data/abq_city_council_districts.geojson --spatial-index --pk=council_district

	touch abq_cannabis_retail_approvals.db

	datasette serve abq_cannabis_retail_approvals.db --load-extension=spatialite
