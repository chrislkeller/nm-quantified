https://github.com/eyeseast/alltheplaces-datasette/blob/main/Makefile

https://bost.ocks.org/mike/make/

https://github.com/datamade/data-making-guidelines/blob/master/make.md



CreationDate: Application submitted online
state_licensed_medical_facility: Whether it's a Active State-licensed Medical Dispensary. If they are, or a microbusiness, they don't have to adhere to the separation requirements.
IDO_District: Integrated Development Ordinance. What is allowable in zones and is available online
name_of_business
state_cannabis_licence_number
ReviewStatus: Still being looked at.


How often updated... instananeus it's updated as applications are submitted. When goes under review...

**Add Council District to retail location**
select distinct
  latest_cannabis_retail_approvals.objectid,
  latest_cannabis_retail_approvals.name_of_business,
  abq_city_council_districts.council_district
from
  latest_cannabis_retail_approvals
left join
  abq_city_council_districts
on
  within(
    latest_cannabis_retail_approvals.Geometry,
    abq_city_council_districts.Geometry
  )
order by
  abq_city_council_districts.council_district asc

**Count by Council Distric**

http://127.0.0.1:8001/abq_cannabis_retail_approvals?sql=select%0D%0A++council_district%2C%0D%0A++count%28council_district%29+as+total%0D%0Afrom%28%0D%0Aselect+distinct%0D%0A++latest_cannabis_retail_approvals.objectid%2C%0D%0A++latest_cannabis_retail_approvals.name_of_business%2C%0D%0A++abq_city_council_districts.council_district+as+council_district%0D%0Afrom%0D%0A++latest_cannabis_retail_approvals%0D%0Aleft+join%0D%0A++abq_city_council_districts%0D%0Aon%0D%0A++within%28%0D%0A++++latest_cannabis_retail_approvals.Geometry%2C%0D%0A++++abq_city_council_districts.Geometry%0D%0A++%29%0D%0Awhere%0D%0A++latest_cannabis_retail_approvals.ReviewStatus+%3D+%27Approved%27%0D%0Aorder+by%0D%0A++abq_city_council_districts.council_district+asc%0D%0A%29%0D%0Agroup+by%0D%0A++council_district%0D%0A

build:
	esri2geojson https://services.arcgis.com/CWv1abTnC3urn4bV/ArcGIS/rest/services/CityCouncil_WNames/FeatureServer/0 abq_city_council_districts.geojson

	geojson-to-sqlite abq_cannabis_retail_approvals.db abq_city_council_districts gis_data/abq_city_council_districts.geojson --spatial-index

	mv abq_city_council_districts.geojson gis_data/abq_city_council_districts.geojson

	geojson-to-sqlite abq_cannabis_retail_approvals.db latest_cannabis_retail_approvals daily-data/latest-abq-cannabis-retail-approvals.geojson --spatial-index

	datasette serve abq_cannabis_retail_approvals.db --load-extension=spatialite
