---
title: "370-F01 ctd sql queries"
source_file: "C:\Users\tchernen\handbook_docx\4_Data_Repository\terrys\370 data handling best practices\370-F01 ctd sql queries.docx"
review_period: "3 years"
created_by: "Terry Curran"
created: "2021-08-19"
modified: "2022-11-07"
---

# Table of Contents

[EXCEL operations [4](#excel-operations)](#excel-operations)

[Add PST string to datetime in Excel [4](#add-pst-string-to-datetime-in-excel)](#add-pst-string-to-datetime-in-excel)

[BASIC Database and Table operations [4](#basic-database-and-table-operations)](#basic-database-and-table-operations)

[PostgreSQL download [4](#_Toc80280389)](#_Toc80280389)

[Check size of tables and objects [4](#check-size-of-tables-and-objects)](#check-size-of-tables-and-objects)

[Copy CSV file to table [4](#copy-csv-file-to-table)](#copy-csv-file-to-table)

[Copy table to CSV file [4](#copy-table-to-csv-file)](#copy-table-to-csv-file)

[Copy table approaches [4](#copy-table-approaches)](#copy-table-approaches)

[1. To copy a table completely [4](#_Toc80280394)](#_Toc80280394)

[2. To copy a table structure without data [5](#_Toc80280395)](#_Toc80280395)

[3. To copy a table with partial data from an existing table [5](#_Toc80280396)](#_Toc80280396)

[Proper names need quotes [5](#proper-names-need-quotes)](#proper-names-need-quotes)

[Find duplicates in a table, id by some columns (Stackoverflow) [5](#find-duplicates-in-a-table-id-by-some-columns-stackoverflow)](#find-duplicates-in-a-table-id-by-some-columns-stackoverflow)

[Select distinct on [5](#select-distinct-on)](#select-distinct-on)

[Create database table with Primary Key [5](#create-database-table-with-primary-key)](#create-database-table-with-primary-key)

[Add a geometry column from lat/long points in table [6](#add-a-geometry-column-from-latlong-points-in-table)](#add-a-geometry-column-from-latlong-points-in-table)

[Add an index [6](#add-an-index)](#add-an-index)

[Set table SRID [6](#set-table-srid)](#set-table-srid)

[Setting parameter based upon nearest match [6](#setting-parameter-based-upon-nearest-match)](#setting-parameter-based-upon-nearest-match)

[Convert (long,lat) to projected points [7](#convert-longlat-to-projected-points)](#convert-longlat-to-projected-points)

[Check your geometry in the classic tuple [7](#check-your-geometry-in-the-classic-tuple)](#check-your-geometry-in-the-classic-tuple)

[Merge data from tables on approximate match [7](#merge-data-from-tables-on-approximate-match)](#merge-data-from-tables-on-approximate-match)

[Selection boxes [8](#selection-boxes)](#selection-boxes)

[1. [geog_geometry && ST_MakeEnvelope 8](#geog_geometry-st_makeenvelope)](#geog_geometry-st_makeenvelope)

[2. [ST_Within and ST_MakeEnvelope 8](#st_within-and-st_makeenvelope)](#st_within-and-st_makeenvelope)

[3. [ST_Within and ST_MakeBox2D 8](#st_within-and-st_makebox2d)](#st_within-and-st_makebox2d)

[TABLE JOINS [9](#table-joins)](#table-joins)

[Select information with outer left join [9](#select-information-with-outer-left-join)](#select-information-with-outer-left-join)

[Select points within polygon in Salish Sea (add semi-colon) [9](#select-points-within-polygon-in-salish-sea-add-semi-colon)](#select-points-within-polygon-in-salish-sea-add-semi-colon)

[Join Bottle data and header [9](#join-bottle-data-and-header)](#join-bottle-data-and-header)

[dfo_bottle_data_2017 [10](#dfo_bottle_data_2017)](#dfo_bottle_data_2017)

[Create ctd linestrings with text as output [10](#_Toc80280417)](#_Toc80280417)

[Add a geometry column [16](#add-a-geometry-column)](#add-a-geometry-column)

[LINESTRING AND POLYGON OPERATIONS [16](#linestring-and-polygon-operations)](#linestring-and-polygon-operations)

[Forming linestring from points [16](#forming-linestring-from-points)](#forming-linestring-from-points)

[Commands to create gps point table and then linestrings [16](#commands-to-create-gps-point-table-and-then-linestrings)](#commands-to-create-gps-point-table-and-then-linestrings)

[Points from GPS to lines 1 [16](#points-from-gps-to-lines-1)](#points-from-gps-to-lines-1)

[Points from GPS to lines 2 [17](#points-from-gps-to-lines-2)](#points-from-gps-to-lines-2)

[Create table for Sidney and James Islands [18](#create-table-for-sidney-and-james-islands)](#create-table-for-sidney-and-james-islands)

[Create database table with line information [19](#create-database-table-with-line-information)](#create-database-table-with-line-information)

[Create ship tracks [19](#create-ship-tracks)](#create-ship-tracks)

[Midpoint on a MultiLineString [19](#midpoint-on-a-multilinestring)](#midpoint-on-a-multilinestring)

[PostGIS Query for a Point Within a Polygon [19](#postgis-query-for-a-point-within-a-polygon)](#postgis-query-for-a-point-within-a-polygon)

[Find point in one table nearest to polygon in another table [20](#find-point-in-one-table-nearest-to-polygon-in-another-table)](#find-point-in-one-table-nearest-to-polygon-in-another-table)

[Updating fields in specific rows with Geometry text [20](#updating-fields-in-specific-rows-with-geometry-text)](#updating-fields-in-specific-rows-with-geometry-text)

[WATER PROPERTY TABLE from tables of header and cast data [20](#water-property-table-from-tables-of-header-and-cast-data)](#water-property-table-from-tables-of-header-and-cast-data)

[Create table cascade for osd ctd data [21](#create-table-cascade-for-osd-ctd-data)](#create-table-cascade-for-osd-ctd-data)

[CREATE TABLE osd_ctd_southern [21](#create-table-osd_ctd_southern)](#create-table-osd_ctd_southern)

[CREATE TABLE osd_ctd_arctic [21](#create-table-osd_ctd_arctic)](#create-table-osd_ctd_arctic)

[CREATE TABLE osd_ctd_atlantic [21](#create-table-osd_ctd_atlantic)](#create-table-osd_ctd_atlantic)

[CREATE TABLE osd_ctd_indian [21](#create-table-osd_ctd_indian)](#create-table-osd_ctd_indian)

[CREATE TABLE osd_ctd_chinasea [21](#create-table-osd_ctd_chinasea)](#create-table-osd_ctd_chinasea)

[CREATE TABLE osd_ctd_pac_west [21](#create-table-osd_ctd_pac_west)](#create-table-osd_ctd_pac_west)

[CREATE TABLE osd_ctd_pac_noreast [21](#create-table-osd_ctd_pac_noreast)](#create-table-osd_ctd_pac_noreast)

[CREATE TABLE osd_ctd_pac_soueast [22](#create-table-osd_ctd_pac_soueast)](#create-table-osd_ctd_pac_soueast)

[CREATE TABLE osd_ctd_ssea [22](#create-table-osd_ctd_ssea)](#create-table-osd_ctd_ssea)

[Rows in partitioned osd_ctd_2017 tables [22](#rows-in-partitioned-osd_ctd_2017-tables)](#rows-in-partitioned-osd_ctd_2017-tables)

[SHOREZONE [22](#shorezone)](#shorezone)

[Add shorezone table [23](#add-shorezone-table)](#add-shorezone-table)

[Create Shorezone track from a series of gps points [23](#create-shorezone-track-from-a-series-of-gps-points)](#create-shorezone-track-from-a-series-of-gps-points)

[PostgreSQL getting daily, weekly, and monthly averages of the occurrences of an event in one query [25](#postgresql-getting-daily-weekly-and-monthly-averages-of-the-occurrences-of-an-event-in-one-query)](#postgresql-getting-daily-weekly-and-monthly-averages-of-the-occurrences-of-an-event-in-one-query)

[Select using “distinct on” and “extract” [25](#select-using-distinct-on-and-extract)](#select-using-distinct-on-and-extract)

[Daily averages [25](#daily-averages)](#daily-averages)

[Weekly averages [26](#weekly-averages)](#weekly-averages)

[Daily averages [26](#daily-averages-1)](#daily-averages-1)

[Daily averages [27](#daily-averages-2)](#daily-averages-2)

[Weekly averages from joined tables [27](#weekly-averages-from-joined-tables)](#weekly-averages-from-joined-tables)

[Weekly averages from joined tables [27](#weekly-averages-from-joined-tables-1)](#weekly-averages-from-joined-tables-1)

[CITIZEN SCIENCE TABLES [28](#citizen-science-tables)](#citizen-science-tables)

[Drop existing table and create new [28](#drop-existing-table-and-create-new)](#drop-existing-table-and-create-new)

[Load table from csv, add geometry column from lat/long [28](#load-table-from-csv-add-geometry-column-from-latlong)](#load-table-from-csv-add-geometry-column-from-latlong)

[WEATHER TABLES [28](#weather-tables)](#weather-tables)

[DROP TABLE IF EXISTS, Create table [28](#drop-table-if-exists-create-table)](#drop-table-if-exists-create-table)

[DROP TABLE IF EXISTS, Create table [29](#drop-table-if-exists-create-table-1)](#drop-table-if-exists-create-table-1)

[FORAGE FISH TABLES [30](#forage-fish-tables)](#forage-fish-tables)

[Create forage fish table [30](#create-forage-fish-table)](#create-forage-fish-table)

# PIT TAG DETECTION TABLES...................................................................................32

##  Very fast query to sort pit detections for dups and uniques....................32

# EXCEL operations

## Add PST string to datetime in Excel

=TEXT(E2,"yyyy-mm-dd hh:mm:ss")&"-8:00"

# 

# BASIC Database and Table operations

<span id="_Toc80280389" class="anchor"></span>PostgreSQL download

https\_\_\_download.postgresql.org_pub_repos_yum_9.6_redhat_rhel-6-x86_64_pgdg-redhat96-9.6-3.noarch.rpm

## 

## Check size of tables and objects 

Check size of tables and objects in PostgreSQL database

SELECT

relname as "Table",

pg_size_pretty(pg_total_relation_size(relid)) As "Size",

pg_size_pretty(pg_total_relation_size(relid) - pg_relation_size(relid)) as "External Size"

FROM pg_catalog.pg_statio_user_tables ORDER BY pg_total_relation_size(relid) DESC;

## 

## Copy CSV file to table

\COPY nodc_ctd_locations FROM F\_\gisData\2014nodcData\ctd\files4export\nodcCtdLocs.csv DELIMITERS , CSV HEADER;

Sample point (no commas or quotes)\_ POINT(-110 30)

## Copy table to CSV file

COPY hab_positioned TO '/home/terry/hab_positioned.csv' DELIMITER ',' CSV HEADER;

\*\*\* since I signed in as postgres, I required pre-existing hab_positioned.csv file (created with VI) and owned by postgres. Also gave full permissions.

## Copy table approaches

<span id="_Toc80280394" class="anchor"></span>1. To copy a table completely, including both table structure and data, you use the following statement:

CREATE TABLE new_table AS

TABLE existing_table;

<span id="_Toc80280395" class="anchor"></span>2. To copy a table structure without data, you add the WITH NO DATA clause to the CREATE TABLE statement as follows:

CREATE TABLE new_table AS

TABLE existing_table

WITH NO DATA;

<span id="_Toc80280396" class="anchor"></span>3. To copy a table with partial data from an existing table, you use the following statement:

CREATE TABLE new_table AS

SELECT \*

FROM existing_table

WHERE condition;

## Proper names need quotes

Select t1.level4name AS name,long,lat,x_utm10n as x,y_utm10n AS y,

t2."VisitDate"::date AS date,t2."StartTime"::TIME AS start, t2."EndTime"::TIME AS end

FROM level4 AS t1

INNER JOIN "Visits" AS t2

ON t1.level4id = t2."Level4ID";

LIMIT 5;

## Find duplicates in a table, id by some columns (Stackoverflow)

SELECT castid,depth, count(\*)

FROM ctd_2017

GROUP BY castid,depth

HAVING count(\*) \> 1;

## Select distinct on

select distinct on (left(castid,7)) \* from osd_ctd_2017

where ST_Within(geog\_\_geometry, ST_GeomFromEWKT(SRID=4326;POLYGON((-126 49,-122 49, -122 50,-126 50, -126 49)))) limit 20;

## Create database table with Primary Key

CREATE TABLE dfo_cast_info(

castID varchar(15) PRIMARY KEY,

mission varchar(20),

event varchar(10),

station varchar(20),

latitude numeric(12,5),

longitude numeric(12,5),

datetime timestamptz,

waterDepth real,

country varchar(20),

project varchar(60),

region varchar(60),

PI varchar(30),

platform varchar(30),

agency varchar(60),

probe_type varchar(30),

instrument varchar(60),

channels smallint,

records smallint,

the_geog geography(POINT, 4326) );

\*\*\* "the_geog" wording is important to QGIS (but not GN or GS)\*\*\*

### Add a geometry column from lat/long points in table

- add a geometry column (quotes for vars),

- add (lat, long) points from the table,

- add index\_

> SELECT AddGeometryColumn (schema,table,geom,4326,POINT,2);
>
> UPDATE table SET geom = ST_SetSRID(ST_MakePoint(long, lat), 4326);

### Add an index

> \*\*\* NEED AN INDEX to find lat_long with GS
>
> CREATE INDEX jacksonco_streets_gix ON jacksonco_streets USING GIST (the_geom);

## Set table SRID

ALTER TABLE mytable

ALTER COLUMN geom

TYPE geometry(Point, 4326)

USING ST_SetSRID(geom, 4326);

## Setting parameter based upon nearest match

with another table field (needs coords with same geom)

UPDATE mabrri_cmn mc

SET phyident = (

SELECT u.phyident

FROM unit_lines u

ORDER BY mc.geom2 \<-\> u.geom

LIMIT 1

);

Explanation:

-----------

Update on mabrri_cmn (cost=0.00..683.67 rows=832 width=1977)

-\> Seq Scan on mabrri_cmn (cost=0.00..683.67 rows=832 width=1977)

SubPlan 1

-\> Limit (cost=0.28..0.61 rows=1 width=46)

-\> Index Scan using unit_lines_gix on unit_lines u (cost=0.28..20245.02 rows=61837 width=46)

Order By: (geom \<-\> mabrri_cmn.geom2), where \<-\> means the distance between the arguments

## Convert (long,lat) to projected points 

With the ST_MakePoint function. It takes the longitude, latitude, and altitude and returns a geometry of type point. Example of such a request:

SELECT ST_MakePoint(longitude,latitude) as geom FROM list_points

Specify the coordinate system (SRID) of your points with the ST_SetSRID function. Example (4326):

SELECT ST_SetSRID(ST_MakePoint(longitude,latitude),4326) as geom FROM list_points

Project your data in a specific coordinate system. Example:

SELECT ST_Transform(ST_SetSRID(ST_MakePoint(longitude,latitude),4326),27561) as geom FROM list_points

## Check your geometry in the classic tuple 

To check your geometry in the classic tuple (longitude,latitude), use the ST_AsText function. For example:

SELECT ST_AsText(geom) as points FROM list_geom

Examine output of converted coordinates with specified SRID, as text

SELECT ST_X(geom) as longitude, ST_Y(geom) as latitude FROM list_geom

## Merge data from tables on approximate match

SELECT

h.island,

h.location,

h.beachnumb,

h.x_utm10n,

h.y_utm10n,

h.species,

h.habitat,

h.length,

h.zone_width,

h.beach_slope,

h.sed_p,

h.sed_s1,

h.sed_s2,

h.sed_depth,

h.sediment AS "sed_continuity",

h.neg_sed,

h.grain_size,

h.vegetation,

h.oh_shading,

h.fs_lu,h.fs_mod,h.fs_struct,

h.bs_lu,h.bs_mod,h.bs_struct,

h.anthro,

h.collection,

sq.island AS s_island,

sq.location_g,sq.location_s,

sq.x_utm10n AS s_x,

sq.y_utm10n AS s_y,

sq.gps_date,

sq.gps_time,

sq.longitude,

sq.latitude,

sq.date_collected,

sq.time_collected,

sq.field_surveyor AS surv,

sq.field_surveyor2 AS surv2,

sq.sediment_c

FROM habitat_descriptors AS h

JOIN LATERAL (

SELECT

s.island,

s.location_g,s,location_s,

s.x_utm10n,s.y_utm10n,

s.gps_date,s.gps_time,

s.longitude,s.latitude,

s.date_collected,s.time_collected,

s.field_surveyor,s.field_surveyor2,

s.sediment_c

FROM gps_static AS s

ORDER BY h.geom_h \<-\> s.geom_s LIMIT 1

) AS sq ON TRUE;

## Selection boxes

All perform quickly, with slight differences between && and ST_Within\[ENVELOPE best\]

### geog_geometry && ST_MakeEnvelope 

> SELECT distinct on (left(castid,7)) \*,st_x(geog\_\_geometry) AS long,st_y(geog\_\_geometry) AS lat from osd_ctd_ssea
>
> WHERE geog\_\_geometry && ST_MakeEnvelope(-126, 49,-122,50,4326) AND depth between 4 and 8 limit 20;

### ST_Within and ST_MakeEnvelope

> select distinct on (left(castid,7)) \*,st_x(geog\_\_geometry) AS long,st_y(geog\_\_geometry) AS lat from osd_ctd_ssea
>
> WHERE ST_Within(geog\_\_geometry, ST_MakeEnvelope(-126, 49,-122,50,4326)) AND depth between 4 and 8 limit 20;

### ST_Within and ST_MakeBox2D

> select distinct on (left(castid,7)) \*,st_x(geog\_\_geometry) AS long,st_y(geog\_\_geometry) AS lat from osd_ctd_ssea WHERE ST_Within(geog\_\_geometry, ST_SetSRID(ST_MakeBox2D(ST_Point(-126, 49),ST_Point(-122,50)),4326)) AND depth between 4 and 8 limit 20;

# TABLE JOINS

## Select information with outer left join

SELECT c.mission AS mission,c.datetime,

d.pressure AS P,d.temperature AS T

FROM dfo_cast_info AS c JOIN dfo_ctd_2017 AS d USING (castid)

GROUP BY mission,datetime,d.pressure,d.temperature limit 20;

## Select points within polygon in Salish Sea (add semi-colon)

SELECT count(\*) from dfo_cast_info where

ST_Within( geog\_\_geometry, ST_GeomFromText(POLYGON ( ( -125.65 50.15, -124.83 51.25, -121.16 47.87, -122.45 47, -123.29 47, -124.86 48.29, -124.27 49.08, -125.65 50.15 ) ), 4326 ) )

## Join Bottle data and header

\COPY osd_bottle_data finalBottle.csv CSV HEADER;

select d.castid,d.depth_metres AS depth,

d.pressurereversing_decibar AS "Prev", d.pressure_decibar AS "P",

d.temperaturereversing_degC_ITS90 AS "Trev",d.temperature_degC_ITS90 AS "T",

d.salinitybottle_pss78 AS "Sbott",d.salinity_pss78 AS "S",

d.oxygendissolved_umol_per_l AS "DO",

h.latitude_deg AS lat, h.longitude_deg AS long

from osd_bottle_data_2017 AS d

inner join osd_bottle_header_2017 AS h ON d.castid=h.castid

where left(d.castid,4)\>'2000' limit 30;

select d.\*,

h.latitude_deg AS lat, h.longitude_deg AS long

from osd_bottle_data_2017 AS d

inner join osd_bottle_header_2017 AS h ON d.castid=h.castid

where left(d.castid,4)\>'2000' limit 30;

select d.\*,

h.latitude_deg AS lat, h.longitude_deg AS long,

h.geom AS geom

from osd_bottle_data_2017 AS d

inner join osd_bottle_header_2017 AS h ON d.castid=h.castid

WHERE h.latitude_deg BETWEEN %latmin% AND %latmax%

AND h.longitude_deg BETWEEN %lonmin% AND %lonmax%

SELECT d.castid, d.depth_metres AS "D",

d.temperature_reversing_degc AS "Trev",d.temperature_degc AS "T",

d.salinity_bottle_psu AS "Sbott",d.salinity_psu AS "S",

d.oxygen_dissolved_umol_l AS "DO",

h.latitude_deg AS lat, h.longitude_deg AS long

FROM osd_bottle_data_2017 AS d

INNER JOIN osd_bottle_header_2017 AS h

ON d.castid=h.castid

WHERE

h.geom && ST_MakeEnvelope(-125,47,-122,50,4326)

AND \_ST_Within(geom, ST_MakeEnvelope(-125,47,-122,50,4326) )

ORDER BY castid limit 10;

SELECT d.\*,

h.latitude_deg AS lat, h.longitude_deg AS long

FROM osd_bottle_data_2017 AS d

INNER JOIN osd_bottle_header_2017 AS h

ON d.castid=h.castid

WHERE

h.geom && ST_MakeEnvelope(-125,47,-122,50,4326)

AND \_ST_Within(geom, ST_MakeEnvelope(-125,47,-122,50,4326) )

ORDER BY castid limit 20;

## dfo_bottle_data_2017

SELECT h.datetime, h.latitude_deg AS lat, h.longitude_deg AS long,

d.\*, h.project, h.pi AS "PI", h.platform, h.station,

h.instType, h.geom

FROM osd_bottle_data_2017 AS d

INNER JOIN osd_bottle_header_2017 AS h

ON d.castid=h.castid

WHERE

h.geom && ST_MakeEnvelope(%lonmin%,%latmin%,%lonmax%,%latmax%, 4326)

AND \_ST_Within(geom, ST_MakeEnvelope(%lonmin%,%latmin%,%lonmax%,%latmax%, 4326) )

ORDER BY h.castid,depth_metres

Data from the "bottle" folders in IOS Archive. Primary data is the nutrient data from water samples. Non-bottle CTD data is from the up-cast. The default latmin, lonmin, laatmax and lonmax parameters can be changed to encompass all readings performed by IOS globally - currently set to Vancouver Island. The first data row contains the count of the number of records in that field, as an indicator of fields to download.

<span id="_Toc80280417" class="anchor"></span>Create ctd linestrings with text as output

CREATE TABLE temp_ctd_ssea AS (

SELECT profile.castid,ST_AsText(profile.geom) AS geom,

ST_AsText(ST_MakeLine(ST_MakePoint(profile.depth, profile.pressure) ORDER BY depth)) AS P,

ST_AsText(ST_MakeLine(ST_MakePoint(profile.depth, profile.temperature) ORDER BY depth)) AS T,

ST_AsText(ST_MakeLine(ST_MakePoint(profile.depth, profile.salinity) ORDER BY depth)) AS S,

ST_AsText(ST_MakeLine(ST_MakePoint(profile.depth, profile.sigma_t) ORDER BY depth)) AS sigma_t,

ST_AsText(ST_MakeLine(ST_MakePoint(profile.depth, profile.sigma_stp) ORDER BY depth)) AS sigma_stp,

ST_AsText(ST_MakeLine(ST_MakePoint(profile.depth, profile.oxygen) ORDER BY depth)) AS oxygen,

ST_AsText(ST_MakeLine(ST_MakePoint(profile.depth, profile.fluor) ORDER BY depth)) AS fluor,

ST_AsText(ST_MakeLine(ST_MakePoint(profile.depth, profile.xmiss) ORDER BY depth)) AS xmiss,

ST_AsText(ST_MakeLine(ST_MakePoint(profile.depth, profile.par) ORDER BY depth)) AS par

FROM osd_ctd_ssea AS profile

GROUP BY profile.castid,profile.geom

);

\*\*\* Create ctd linestrings with hex as output

CREATE TABLE temp_ctd_ssea AS (

SELECT profile.castid,profile.geom AS geom,

ST_MakeLine(ST_MakePoint(profile.depth, profile.pressure) ORDER BY depth) AS P,

ST_MakeLine(ST_MakePoint(profile.depth, profile.temperature) ORDER BY depth) AS T,

ST_MakeLine(ST_MakePoint(profile.depth, profile.salinity) ORDER BY depth) AS S,

ST_MakeLine(ST_MakePoint(profile.depth, profile.sigma_t) ORDER BY depth) AS sigma_t,

ST_MakeLine(ST_MakePoint(profile.depth, profile.sigma_stp) ORDER BY depth) AS sigma_stp,

ST_MakeLine(ST_MakePoint(profile.depth, profile.oxygen) ORDER BY depth) AS oxygen,

ST_MakeLine(ST_MakePoint(profile.depth, profile.fluor) ORDER BY depth) AS fluor,

ST_MakeLine(ST_MakePoint(profile.depth, profile.xmiss) ORDER BY depth) AS xmiss,

ST_MakeLine(ST_MakePoint(profile.depth, profile.par) ORDER BY depth) AS par

FROM osd_ctd_ssea AS profile

GROUP BY profile.castid,profile.geom

);

CREATE TABLE ios_bottle_2017 (

castID varchar(30),

datetime timestamptz,

project varchar(50),

area varchar(50),

mission varchar(10),

PI varchar(30),

platform varchar(30),

station varchar(40),

event varchar(10),

longitude_deg real,

latitude_deg real,

waterDepth_metres varchar(20),

agency varchar(50),

country varchar(20),

dataDesc varchar(60),

instType varchar(50),

instModel varchar(30),

instSN varchar(10),

chans smallint,

recs smallint,

bin_records smallint,

Sample_Number varchar(10),

Depth_metres real \[ \],

Pressure_decibar real \[ \],

Temperature_degC_ITS90 real \[ \],

"Temperature_Reversing_deg C (IPTS68)" real \[ \],

"Temperature_BT_deg C" real \[ \],

"Temperature_Bucket_deg C (IPTS68)" real \[ \],

"Temperature_DoDraw_deg C (ITS90)" real \[ \],

"Salinity_Bottle_PSS-78" real \[ \],

Salinity real \[ \],

"Oxygen_Dissolved_Mass_umol_kg" real \[ \],

"Oxygen_Dissolved_mL_L" real \[ \],

"Oxygen_Dissolved_Saturation\_%" real \[ \],

"Oxygen_Isotope_18\_\_mille" real \[ \],

"Transmissivity\_%\_metre" real \[ \],

"Turbidity_Seapoint_FTU" real \[ \],

"Total_Suspended_Solids_mg_m3" real \[ \],

"PAR_uE_m^2_sec" real \[ \],

"PAR_Reference_uE_m^2_sec" real \[ \],

pH real \[ \],

"Alkalinity_Total_CRM_Corrected_umol_kg" real \[ \],

"Alkalinity_Carbonate_umol_kg" real \[ \],

"Calcium_Total_mmol_kg" real \[ \],

"Chlorophyll_Extracted_mg_m^3" real \[ \],

"Phaeo-Pigment_Extracted_mg_m^3" real \[ \],

"Chlorophyll_plus_Phaeo-Pigment_Extracted_mg_m^3" real \[ \],

"Chlorophyll_Extracted\_\>0.7um_mg_m^3" real \[ \],

"Chlorophyll_Extracted\_\>5.0um_mg_m^3" real \[ \],

"Chlorophyll_Extracted\_\<5.0um_mg_m^3" real \[ \],

"CDOM_mg_m^3" real \[ \],

"Fluorescence_mg_m^3" real \[ \],

"Phosphate_umol_L" real \[ \],

"Silicate_umol_L" real \[ \],

"Silicate_Acidified_umol_L" real \[ \],

"Ammonium_umol_L" real \[ \],

"Nitrate_umol_L" real \[ \],

"Nitrite_umol_L" real \[ \],

"Nitrate_plus_Nitrite_umol_L" real \[ \],

"Nitrogen_Particulate_Total_umol_kg" real \[ \],

"Nitrogen_Particulate_Organic_mg_m^3" real \[ \],

"Nitrogen_Dissolved_Organic_umol_L" real \[ \],

"Carbon_Particulate_Total_umol_L" real \[ \],

"Carbon_Particulate_Organic_mg_m^3" real \[ \],

"Carbon_Dissolved_Organic_umol_L" real \[ \],

"Carbon_Dissolved_Inorganic_umol_kg" real \[ \],

"Carbon_Total_Organic_umol_kg" real \[ \],

"Carbon_Isotope_13\_\_mille" real \[ \],

"Carbon_Isotope_14\_\_mille" real \[ \],

"Production_Primary_day_mgC_m^3_day" real \[ \],

"Production_Primary_hr_mgC_m^3_hour" real \[ \],

"Bacteria1_10^6_mL" real \[ \],

"Bacteria2\_\_mL" real \[ \],

"Picophytoplankton\_\_mL" real \[ \],

"Nanophytoplankton\_\_mL" real \[ \]

);

\COPY ios_bottle_2017 FROM F\_\gisData\2017Oct_osd\osdResult\20171126_163757_compressed.csv CSV HEADER;

CREATE TABLE osd_bottle_header (

castID varchar(30),

datetime timestamptz,

project varchar(60),

area varchar(60),

mission varchar(10),

PI varchar(30),

platform varchar(30),

station varchar(40),

event varchar(10),

longitude_deg real,

latitude_deg real,

waterDepth_metres varchar(20),

agency varchar(60),

country varchar(20),

dataDesc varchar(60),

instType varchar(50),

instModel varchar(30),

instSN varchar(10),

chans smallint,

recs smallint,

bin_records varchar(10),

Depth_metres real \[ \],

Pressure_Reversing_decibar real \[ \],

Pressure_decibar real \[ \],

Temperature_Reversing_degC real \[ \],

Temperature_degC real \[ \],

Temperature_BT_degC real \[ \],

Temperature_Bucket_degC real \[ \],

Temperature_Draw_degC real \[ \],

Salinity_Bottle_PSU real \[ \],

Salinity_PSU real \[ \],

Sigma_t real \[ \],

Turbidity_Seapoint_FTU real \[ \],

Total_Suspended_Solids_mg_L real \[ \],

Transmissivity_pc_metre real \[ \],

Oxygen_Dissolved_umol_L real \[ \],

Oxygen_Dissolved_Mass_umol_kg real \[ \],

Oxygen_Dissolved_Saturation_pc real \[ \],

Oxygen_Isotope_18\_\_mille real \[ \],

PAR_uE_m2_sec real \[ \],

PAR_Reference_uE_m2_sec real \[ \],

pH real \[ \],

Fluorescence_mg_m3 real \[ \],

CDOM_mg_m3 real \[ \],

Chlorophyll_Extracted_mg_m3 real \[ \],

Chlorophyll_Extracted_lt5um_mg_m3 real \[ \],

Chlorophyll_Extracted_gtpoint7um_mg_m3 real \[ \],

Chlorophyll_Extracted_gt5um_mg_m3 real \[ \],

Chlorophyll_Extracted_point3um_mg_m3 real \[ \],

Phaeo_Pigment_Extracted_mg_m3 real \[ \],

Phaeo_Pigment_Extracted_point3um_mg_m3 real \[ \],

Chlorophyll_plus_Phaeo_Pigment_Extracted_mg_m3 real \[ \],

Nitrogen_Dissolved_Organic_umol_L real \[ \],

Nitrogen_Particulate_Organic_mg_m3 real \[ \],

Nitrogen_Particulate_Total_umol_L real \[ \],

Nitrate_umol_L real \[ \],

Nitrite_umol_L real \[ \],

Nitrate_plus_Nitrite_umol_L real \[ \],

Phosphate_umol_L real \[ \],

Silicate_umol_L real \[ \],

Silicate_Acidified_umol_L real \[ \],

Ammonium_umol_L real \[ \],

Alkalinity_Total_umol_kg real \[ \],

Alkalinity_Total_Colorimetric_umol_kg real \[ \],

Alkalinity_Total_Potentiometric_umol_kg real \[ \],

Alkalinity_Carbonate_umol_kg real \[ \],

Production_Primary_mgC_m3_day real \[ \],

Bacteria_million_mL real \[ \],

Carbon_Dissolved_Inorganic_umol_kg real \[ \],

Carbon_Dissolved_Organic_umol_L real \[ \],

Carbon_Particulate_Organic_umol_L real \[ \],

Carbon_Particulate_Total_umol_L real \[ \],

Carbon_Total_Organic_umol_L real \[ \],

Carbon_Isotope_13\_\_mille real \[ \],

Carbon_Isotope_14\_\_mille real \[ \],

Aluminum_Dissolved_pmol_L real \[ \],

Calcium_Total_mmol_kg real \[ \],

Iron_Filtered_Buffered_point_03_nmol_L real \[ \],

Iron_Filtered_Buffered_point_1_nmol_L real \[ \],

Iron_Filtered_Buffered_point_22_nmol_L real \[ \],

Iron_Filtered_Buffered_point_45_nmol_L real \[ \],

Iron_Filtered_Buffered_200kDalton_nmol_L real \[ \],

Iron_Filtered_StrongAcid_point_22_nmol_L real \[ \],

Iron_Filtered_StrongAcid_Geo_point_22_nmol_L real \[ \],

Iron_Filtered_StrongAcid_MV_point_22_nmol_L real \[ \],

Iron_Unfiltered_Buffered_nmol_L real \[ \],

Iron_Unfiltered_Geo_StrongAcid_nmol_L real \[ \],

Iron_Unfiltered_StrongAcid_nmol_L real \[ \],

Iron_Unfiltered_StrongAcid_MV_nmol_L real \[ \],

Sample_Number varchar(10)

);

CREATE TABLE osd_bottle_data_2017 (

castID varchar(30),

Depth_metres numeric(10,1),

Pressure_Reversing_decibar numeric(10,1),

Pressure_decibar numeric(10,1),

Temperature_Reversing_degC numeric(10,3),

Temperature_degC numeric(10,3),

Temperature_BT_degC numeric(10,3),

Temperature_Bucket_degC numeric(10,3),

Temperature_Draw_degC numeric(10,3),

Salinity_Bottle_PSU numeric(10,3),

Salinity_PSU numeric(10,3),

Sigma_t numeric(10,3),

Turbidity_Seapoint_FTU numeric(10,1),

Total_Suspended_Solids_mg_L numeric(10,1),

Transmissivity_pc_metre numeric(10,2),

Oxygen_Dissolved_umol_L numeric(10,2),

Oxygen_Dissolved_Mass_umol_kg numeric(10,1),

Oxygen_Dissolved_Saturation_pc real,

Oxygen_Isotope_18\_\_mille real,

PAR_uE_m2_sec numeric(10,3),

PAR_Reference_uE_m2_sec numeric(10,3),

pH numeric(10,4),

Fluorescence_mg_m3 numeric(10,3),

CDOM_mg_m3 numeric(10,3),

Chlorophyll_Extracted_mg_m3 numeric(10,3),

Chlorophyll_Extracted_lt5um_mg_m3 numeric(10,3),

Chlorophyll_Extracted_gtpoint7um_mg_m3 numeric(10,3),

Chlorophyll_Extracted_gt5um_mg_m3 numeric(10,3),

Chlorophyll_Extracted_point3um_mg_m3 numeric(10,3),

Phaeo_Pigment_Extracted_mg_m3 numeric(10,3),

Phaeo_Pigment_Extracted_point3um_mg_m3 numeric(10,3),

Chlorophyll_plus_Phaeo_Pigment_Extracted_mg_m3 numeric(10,3),

Nitrogen_Dissolved_Organic_umol_L numeric(10,3),

Nitrogen_Particulate_Organic_mg_m3 numeric(10,3),

Nitrogen_Particulate_Total_umol_L numeric(10,3),

Nitrate_umol_L numeric(10,3),

Nitrite_umol_L numeric(10,3),

Nitrate_plus_Nitrite_umol_L numeric(10,3),

Phosphate_umol_L numeric(10,3),

Silicate_umol_L numeric(10,3),

Silicate_Acidified_umol_L numeric(10,3),

Ammonium_umol_L numeric(10,3),

Alkalinity_Total_umol_kg numeric(10,3),

Alkalinity_Total_Colorimetric_umol_kg numeric(10,3),

Alkalinity_Total_Potentiometric_umol_kg numeric(10,3),

Alkalinity_Carbonate_umol_kg numeric(10,3),

Production_Primary_mgC_m3_day numeric(10,3),

Bacteria_million_mL numeric(10,3),

Carbon_Dissolved_Inorganic_umol_kg numeric(10,3),

Carbon_Dissolved_Organic_umol_L numeric(10,3),

Carbon_Particulate_Organic_umol_L numeric(10,3),

Carbon_Particulate_Total_umol_L numeric(10,3),

Carbon_Total_Organic_umol_L numeric(10,3),

Carbon_Isotope_13\_\_mille numeric(10,3),

Carbon_Isotope_14\_\_mille numeric(10,3),

PhytoplanktonVolume_mm3_per_m3 numeric(10,3),

Nanophytoplankton_per_mL numeric(10,3),

Picophytoplankton_per_mL numeric(10,3),

Aluminum_Dissolved_pmol_L numeric(10,3),

Calcium_Total_mmol_kg numeric(10,3),

Iron_Filtered_Buffered_point_03_nmol_L numeric(10,3),

Iron_Filtered_Buffered_point_1_nmol_L numeric(10,3),

Iron_Filtered_Buffered_point_22_nmol_L numeric(10,3),

Iron_Filtered_Buffered_point_45_nmol_L numeric(10,3),

Iron_Filtered_Buffered_200kDalton_nmol_L numeric(10,3),

Iron_Filtered_StrongAcid_point_22_nmol_L numeric(10,3),

Iron_Filtered_StrongAcid_Geo_point_22_nmol_L numeric(10,3),

Iron_Filtered_StrongAcid_MV_point_22_nmol_L numeric(10,3),

Iron_Unfiltered_Buffered_nmol_L numeric(10,3),

Iron_Unfiltered_Geo_StrongAcid_nmol_L numeric(10,3),

Iron_Unfiltered_StrongAcid_nmol_L numeric(10,3),

Iron_Unfiltered_StrongAcid_MV_nmol_L numeric(10,3),

Sample_Number varchar(10)

);

\*\*\*

## Add a geometry column

- add a geometry column,

- add (lat, long) points from the table,

- add index\_

SELECT AddGeometryColumn ('data','osd_bottle_2017','geom',4326,'POINT',2);

UPDATE table SET geom = ST_SetSRID(ST_MakePoint(long, lat), 4326);

# LINESTRING AND POLYGON OPERATIONS

## Forming linestring from points

-- If you are using PostgreSQL 9.0+

-- (you can use the new ORDER BY support for aggregates)

-- this is a guaranteed way to get a correctly ordered linestring

-- Your order by part can order by more than one column if needed

SELECT gps.gps_track, ST_MakeLine(gps.the_geom ORDER BY gps_time) As newgeom

FROM gps_points As gps

GROUP BY gps.gps_track;

## Commands to create gps point table and then linestrings

### Points from GPS to lines 1

drop table gps_dynamic ;

create table gps_dynamic(

Island varchar,

LineNo integer,

Point_ID varchar,

GPS_Date date,

GPS_Time time,

Latitude numeric(12,5),

Longitude numeric(12,5),

GNSS_Heigh varchar,

X_UTM10N numeric(10,1),

Y_UTM10N numeric(10,1),

Max_PDOP varchar,

Max_HDOP varchar,

Datafile varchar,

Corr_Type varchar,

Rcvr_Type varchar,

Update_Sta varchar,

Feat_Name varchar,

Unfilt_Pos varchar,

Filt_Pos varchar,

Vert_Prec varchar,

Horz_Prec varchar,

dist real,

deldist real,

deltime real,

LineFlag numeric(5,0)

);

\COPY gps_dynamic from './20190914_dynamic.csv' DELIMITER ',' CSV HEADER;

alter table gps_dynamic add column gid serial primary key;

alter table gps_dynamic add column geom_d geometry(Point,26910);

update gps_dynamic set geom_d = ST_SetSRID(ST_MakePoint(x_utm10n,y_utm10n),26910);

create index dyn_gix ON gps_dynamic USING GIST(geom_d);

### Points from GPS to lines 2

CREATE TABLE gps_tracks AS SELECT gps.island AS island,gps.lineno,min(gps.gps_date) AS date_start, min(gps.gps_time) AS time_start, max(gps.gps_date) AS date_end, max(gps.gps_time) AS time_end,gps.datafile,ST_MakeLine(gps.geom_d ORDER BY gps_time) As geom2

FROM gps_dynamic As gps

GROUP BY (gps.island,gps.lineno,gps.gps_date,gps.datafile);

delete from gps_tracks where time_start=time_end;

alter table gps_tracks add column geom geometry(LineString, 26910);

update gps_tracks set geom = ST_Transform(geom2, 26910);

alter table gps_tracks drop column geom2;

\d gps_tracks

select island,lineno,date_start AS date,time_start,time_end,(time_end-time_start) AS del_t,datafile,left(ST_AsText(geom),50)

FROM gps_tracks

Order BY lineno;

alter table gps_tracks add column gid serial primary key;

create index gps_tracks_gix on gps_tracks using gist(geom);

\d gps_tracks

### Create table for Sidney and James Islands

create table isle_trust_sidney_james (

OBJECTID varchar,

Species varchar,

BeachNumb varchar,

Island varchar,

Location varchar,

Sample_Date date,

Sample_Time time,

WP_POSITION varchar,

UTM_Zone varchar,

y_utm10n numeric(10,1),

x_utm10n numeric(10,1),

GPS_Model varchar,

Habitat varchar,

Sediment varchar,

Anthro varchar,

Neg_Sed varchar,

Sed_P varchar,

Sed_S1 varchar,

Sed_S2 varchar,

OH_Shading varchar,

Vegetation varchar,

FS_Mod varchar,

FS_Struct varchar,

FS_LU varchar,

BS_Mod varchar,

BS_Struct varchar,

BS_LU varchar,

Beach_Slope varchar,

Zone_Width numeric(10,1),

Beach_Length numeric(10,1),

Sed_Depth varchar,

Tide_Height varchar,

Description varchar,

SHAPE_Length varchar,

geom geometry(Linestring, 26910)

);

\COPY isle_trust_sidney_james from './sidney_james_wkt_geom_26910.csv' DELIMITER ',' CSV HEADER;

alter table isle_trust_sidney_james add column gid serial primary key;

alter table isle_trust_sidney_james add column geom_pt geometry(Point,26910);

update isle_trust_sidney_james set geom_pt =ST_SetSRID(ST_MakePoint(x_utm10n,y_utm10n),26910);

### Create database table with line information

CREATE TABLE dfo_missions AS

SELECT mission, min(datetime) AS start, max(datetime) AS finish,

project, investigator AS pi, platform,

ST_MakeLine((geog\_\_geometry) ORDER BY datetime) As shiptrack

FROM dfo_cast_info GROUP BY mission,project,pi,platform;

### Create ship tracks

CREATE TABLE nodc_ship_tracks AS

SELECT nodcid, accessionNo, country, institute, cruiseid AS orig cruise ID,

project, investigator AS PI, platform, min(datetime) AS start, max(datetime) AS finish,

instrument, ST_MakeLine(the_geog\_\_geometry ORDER BY datetime) As track

FROM nodc_ctd_info

GROUP BY nodcid,cruiseid,project,PI,platform,instrument,accessionNo,country,institute;

## 

### Midpoint on a MultiLineString

select organization,

ST_X(ST_Transform(ST_LineInterpolatePoint(ST_LineMerge(geom),0.5),4326)) AS "Long",

ST_Y(ST_Transform(ST_LineInterpolatePoint(ST_LineMerge(geom),0.5),4326)) AS "Lat",

ST_XMIN(geom),ST_YMIN(geom),sed_continuity from ff_it limit 100;

## 

### PostGIS Query for a Point Within a Polygon

CREATE or replace function in_neighborhood(coords varchar(255))

returns varchar(255)

as \$\$

declare

myid varchar(255);

begin

SELECT id FROM zones

WHERE ST_Contains(zones.geometry, ST_Transform(

ST_GeomFromText(concat(POINT(, coords, )), 4326), 4326)

)

into myid;

return myid;

end;

\$\$

language plpgsql;

## 

### Find point in one table nearest to polygon in another table

PostGIS - For each polygon/linestring/point in table A, find nearest point in table B and update table A with value

UPDATE tableA tA1

SET pc = (SELECT near_point.pc

FROM tableA tA2, LATERAL

(SELECT pc

FROM tableB

ORDER BY tableB.geom \<-\> tA2.geom

LIMIT 1) near_point

WHERE tA2.id = tA1.id)

UPDATE table

SET column1 = value1,

column2 = value2 ,...

WHERE

condition;

UPDATE dfo_cast_info SET investigator=value1 WHERE condition;

## Updating fields in specific rows with Geometry text

shorezone=\> update ff_spawning_beach_monitoring

shorezone-\> set geom=ST_TRANSFORM(ST_GeomFromEWKT('SRID=4326;MULTILINESTRING((-124.198203173111 49.2964658229472,-124.198282979567 49.2963568746907,-124.198283741357 49.2962488586613,-124.198338085901 49.2961763414833,-124.198114217154 49.2958820011725,-124.198002368637 49.29562215362,-124.198001085456 49.2954783818015,-124.198058873572 49.2954056340535,-124.198170994402 49.2952606479666,-124.198619254441 49.2950399758336,-124.198675663273 49.2949584813958,-124.198843377444 49.2949297784894,-124.199069534956 49.2948556152432,-124.199180902105 49.2948183743756,-124.199461729513 49.2947074285786,-124.199909539913 49.2946307732101,-124.200020895371 49.2945938013618,-124.20047007067 49.2945261778479,-124.200583152644 49.2944889551128,-124.200806192267 49.2944507549769,-124.201200415059 49.2943385964874,-124.201424528541 49.2942283936728,-124.201535892642 49.2941911413462,-124.201760004614 49.2940809378113,-124.202210595402 49.2939322999747,-124.20237862541 49.2939395975428,-124.202603055723 49.2938654072241,-124.203051185515 49.2938244748507,-124.203163180172 49.2938595387274,-124.203997546921 49.2938236130465))'),26910)

WHERE phyident='01/10/0099/00';

# WATER PROPERTY TABLE from tables of header and cast data 

Water property casts via a profiling CTD always include castid, datetime, longitude, latitude, depth, pressure and temperature. It almost always includes salinity, sigma-t and sigma-Stp (density anomaly). It often includes oxygen and fluorescence. It may include PAR.

CREATE TABLE temp_ctd_2017 AS

SELECT c.castID AS castid,depth,pressure,temperature,salinity,sigma_t,sigma_stp,oxygen,fluor,xmiss_m AS xmiss,par,geog from dfo_cast_info AS c INNER JOIN ctd_2017 USING (castid)

PRIMARY KEY (castid, depth)

);

## Create table cascade for osd ctd data

### CREATE TABLE osd_ctd_southern

(LIKE temp_ctd_2017 INCLUDING DEFAULTS INCLUDING CONSTRAINTS);

ALTER TABLE osd_ctd_southern ADD CONSTRAINT ocean_southern

CHECK (ST_Y(geog\_\_geometry) \<-45);

alter table osd_ctd_southern add column fid serial PRIMARY KEY

### CREATE TABLE osd_ctd_arctic

(LIKE temp_ctd_2017 INCLUDING DEFAULTS INCLUDING CONSTRAINTS);

ALTER TABLE osd_ctd_arctic ADD CONSTRAINT ocean_arctic

CHECK (ST_Y(geog\_\_geometry) \>65 );

### CREATE TABLE osd_ctd_atlantic

(LIKE temp_ctd_2017 INCLUDING DEFAULTS INCLUDING CONSTRAINTS);

ALTER TABLE osd_ctd_atlantic ADD CONSTRAINT ocean_atlantic

CHECK ( (ST_Y(geog\_\_geometry) BETWEEN -45 AND +65) AND

(ST_X(geog\_\_geometry) between -80.001 and +21) );

###  CREATE TABLE osd_ctd_indian

(LIKE temp_ctd_2017 INCLUDING DEFAULTS INCLUDING CONSTRAINTS);

ALTER TABLE osd_ctd_indian ADD CONSTRAINT ocean_indian

CHECK ( (ST_Y(geog\_\_geometry) BETWEEN -45 AND +65) AND

(ST_X(geog\_\_geometry) between 21.001 and 100) );

### CREATE TABLE osd_ctd_chinasea

(LIKE temp_ctd_2017 INCLUDING DEFAULTS INCLUDING CONSTRAINTS);

ALTER TABLE osd_ctd_chinasea ADD CONSTRAINT ocean_chinasea

CHECK ( (ST_Y(geog\_\_geometry) BETWEEN -45 AND +65) AND

(ST_X(geog\_\_geometry) between 122.001 and 125) );

### CREATE TABLE osd_ctd_pac_west

(LIKE osd_ctd_2017 INCLUDING DEFAULTS INCLUDING CONSTRAINTS);

ALTER TABLE osd_ctd_pac_west ADD CONSTRAINT ocean_pacw

CHECK ( (ST_Y(geog\_\_geometry) BETWEEN -45 AND +65) AND (ST_X(geog\_\_geometry) BETWEEN 125.001 and 180) );

### CREATE TABLE osd_ctd_pac_noreast

(LIKE osd_ctd_2017 INCLUDING DEFAULTS INCLUDING CONSTRAINTS);

ALTER TABLE osd_ctd_pac_noreast ADD CONSTRAINT ocean_pacne

CHECK ( (ST_Y(geog\_\_geometry) BETWEEN 51.5 AND +65) AND (ST_X(geog\_\_geometry) BETWEEN -180 and -80) );

### CREATE TABLE osd_ctd_pac_soueast

(LIKE osd_ctd_2017 INCLUDING DEFAULTS INCLUDING CONSTRAINTS);

ALTER TABLE osd_ctd_pac_soueast ADD CONSTRAINT ocean_pacse

CHECK ( (ST_Y(geog\_\_geometry) BETWEEN -45 AND +51.499999) AND (ST_X(geog\_\_geometry) BETWEEN -180 and -80) AND NOT ST_Within( geog\_\_geometry, ST_GeomFromText(POLYGON ( ( -125.65 50.15, -124.83 51.25, -121.16 47.87, -122.45 47, -123.29 47, -124.86 48.29, -124.27 49.08, -125.65 50.15 ) ), 4326 ) ) );

### CREATE TABLE osd_ctd_ssea

(LIKE temp_ctd_2017 INCLUDING DEFAULTS INCLUDING CONSTRAINTS);

ALTER TABLE osd_ctd_ssea ADD CONSTRAINT ocean_ssea

CHECK ( ST_Within( geog\_\_geometry, ST_GeomFromText(POLYGON ( ( -125.65 50.15, -124.83 51.25, -121.16 47.87, -122.45 47, -123.29 47, -124.86 48.29, -124.27 49.08, -125.65 50.15 ) ), 4326 ) ) );

INSERT INTO osd_ctd_pac_west(castid,depth,pressure,temperature,salinity,sigma_t,sigma_stp,oxygen,fluor,xmiss,par,geog)

SELECT castid,depth,pressure,temperature,salinity,sigma_t,sigma_stp,oxygen,fluor,xmiss,par,geog

FROM osd_ctd_pacific

WHERE ( (ST_Y(geog\_\_geometry) BETWEEN -45 AND +65) AND (ST_X(geog\_\_geometry) BETWEEN 125.001 and 180) );

### Rows in partitioned osd_ctd_2017 tables

osd_ctd_2017 = 6 744 812

osd_ctd_arctic = 3 932 330

osd_ctd_atlantic = 23 434

osd_ctd_chinasea = 0

osd_ctd_indian = 0

osd_ctd_pac_noreast = 3 436 687

osd_ctd_pac_soueast = 16 834 965

osd_ctd_pac_west = 1 876 355

osd_ctd_southern = 83 641

osd_ctd_ssea = 2 705 407

osd_ctd_pacific = 22 148 007

# SHOREZONE

ShoreZone is an aerial imaging, coastal habitat classification and mapping system used to inventory alongshore and across-shore geomorphological and biological attributes of the shoreline. The georeferenced, oblique, low altitude aerial imagery is acquired during the lowest tides of the year and then used to classify habitat attributes into a searchable database. This data is used for coastal planning, identification of vulnerable resources, oil spill response planning, habitat modeling, recreational planning and scientific research.

Each Shorezone bioband is an assemblage of coastal biota, and are visible in aerial imagery as patterns of colour and texture across the shoreline. Biobands are generally associated with characteristic wave energies, substrate conditions and across-shore elevations, and are often seen as spatially distinct alongshore and across-shore patterns. Each bioband is named for the dominant species or group.

## Add shorezone table

CREATE TABLE shorezone_track_sample (

FID integer,

LAT real,

LON real,

DATE_UTC date,

TIME_UTC time,

DATETIME timestamp,

TAPE_NO varchar,

PLAY_VIDEO varchar,

PHOTONAME varchar,

VIEW_PHOTO varchar,

DISPLAY varchar );

## Create Shorezone track from a series of gps points

\COPY shorezone_track_sample FROM 'F:\gisData\2017_11_17 CORI_BcShoreZone\trackline\bc15_sh_ShoreZone_track.csv' CSV HEADER;

This example takes a sequence of GPS points and creates one record for each gps travel where the geometry field is a line string composed of the gps points in the order of the travel.

-- If you are using PostgreSQL 9.0+

-- (you can use the new ORDER BY support for aggregates)

-- this is a guaranteed way to get a correctly ordered linestring

-- Your order by part can order by more than one column if needed

SELECT gps.gps_track, ST_MakeLine(gps.the_geom ORDER BY gps_time) As newgeom

FROM gps_points As gps

GROUP BY gps.gps_track;

SELECT ST_MakeLine(gps.geom ORDER BY datetime) As newgeom

FROM shorezone_track_sample As gps

GROUP BY gps.track;

CREATE TABLE cori_tracks AS

SELECT gps.tape_no, min(datetime) AS start, max(datetime) AS finish,

ST_MakeLine(gps.geom ORDER BY gps.datetime) As trackgeom

FROM shorezone_track_sample As gps

GROUP BY gps.tape_no;

SELECT l.unit_id,b.\*,l.geom

FROM unit_lines AS l

INNER JOIN bioband AS b

ON l.phyident=b.phyident

# 

# PostgreSQL getting daily, weekly, and monthly averages of the occurrences of an event in one query

(https://stackoverflow.com/questions/38226788/postgresql-getting-daily-weekly-and-monthly-averages-of-the-occurrences-of-an/38227758)

CURRENTLY: I have this rather large query that works by

\* Aggregating the daily, weekly, monthly counts into intermediate tables by taking the count() of an event grouped by the event name and the date.

\* Selecting the avg count over each intermediate table by doing avg() group by just event, doing a union of the results,

and because I want to have a separate column for daily, weekly, monthly, putting a filler value of 0 into empty columns.

\* I then sum over all the columns, and the 0s basically act as a no-op, which gives me just a single value for each event.

ANSWER: In 9.5+ use grouping sets

The data selected by the FROM and WHERE clauses is grouped separately by each specified grouping set, aggregates computed for each group just as for simple GROUP BY clauses, and then the results returned

select event,

avg(total) filter (where day is not null) as avg_day,

avg(total) filter (where week is not null) as avg_week,

avg(total) filter (where month is not null) as avg_month

from (

select

event,

date_trunc('day', created_at) as day,

date_trunc('week', created_at) as week,

date_trunc('month', created_at) as month,

count(\*) as total

from tracking_stuff

where event in ('thing','thing2','thing3')

group by grouping sets ((event, 2), (event, 3), (event, 4))

) s

group by event

## Select using “distinct on” and “extract”

### Daily averages

select distinct on (extract(day from date)) s.stnid,s.station,

longitude AS "lon",latitude AS "lat",date,temp,temp_sd,press,p_sd,

dew_pt,"RH",wind_min,wind_max,avg AS wind_avg,stddev AS wind_sd,vis

from weather_daily w inner join weather_stations s on (w.stnid=s.stnid)

order by lat desc

limit 100;

### Weekly averages

select distinct ON (extract(week from to_date(dt,'yyyy-mm-dd')) )

stnid,station,

to_date(dt,'yyyy-mm-dd') AS "date",

min(wind) AS "wind_min",max(wind) AS "wind_max",

SQRT(POWER(AVG(-wind\*COS(RADIANS(wind_dir_10s \* 10 ) ) ),2 ) +

POWER(AVG(-wind\*SIN(RADIANS(wind_dir_10s \* 10 ) ) ),2 ) )::numeric(7,1) AS "wind_avg",

90 - DEGREES(ATAN2(AVG(-wind\*COS(RADIANS(wind_dir_10s \* 10 ))),

AVG(-wind\*SIN(RADIANS(wind_dir_10s \* 10 )))) )::numeric(7,1) AS "wind_to_dir",

AVG(-wind\*SIN(RADIANS(wind_dir_10s \* 10 ) ) )::numeric(7,1) AS "wnd_eward",

AVG(-wind\*COS(RADIANS(wind_dir_10s \* 10 ) ) )::numeric(7,1) AS "wnd_nthward"

from weather_hourly

group by stnid, station,to_date(dt,'yyyy-mm-dd')

limit 100;

### Daily averages

CREATE TABLE weather_daily AS

select stnid,station,

to_date(dt,'yyyy-mm-dd') AS "date",

AVG(temp)::numeric(7,2) AS "temp",stddev(temp)::numeric(5,1) AS "temp_sd",

AVG(dew_point)::numeric(5,1) AS "dew_pt", AVG(rel_hum_pc)::numeric(5,1) AS "rh",

AVG(press)::numeric(5,1) AS "press",stddev(press)::numeric(5,1) AS "p_sd",

AVG(visibility)::numeric(7,1) AS "vis",

min(wind) AS "wind_min",max(wind) AS "wind_max",

SQRT(POWER(AVG(-wind\*COS(RADIANS(wind_dir_10s \* 10 ) ) ),2 ) +

POWER(AVG(-wind\*SIN(RADIANS(wind_dir_10s \* 10 ) ) ),2 ) )::numeric(7,1) AS "wind_avg",

90 - DEGREES(ATAN2(AVG(-wind\*COS(RADIANS(wind_dir_10s \* 10 ))),

AVG(-wind\*SIN(RADIANS(wind_dir_10s \* 10 )))) )::numeric(7,1) AS "wind_to_dir",

AVG(-wind\*SIN(RADIANS(wind_dir_10s \* 10 ) ) )::numeric(7,1) AS "wnd_eward",

AVG(-wind\*COS(RADIANS(wind_dir_10s \* 10 ) ) )::numeric(7,1) AS "wnd_nthward"

from weather_hourly

group by stnid, station,to_date(dt,'yyyy-mm-dd')

### Daily averages

select \*

from weather_stations s, weather_daily d

where d.stnid=s.stnid

limit 300;

### Weekly averages from joined tables

select distinct on (extract(week from date) )

station, longitude AS "lon", latitude AS "lat", elevation_m AS "ht",

s.stnid, date,temp, dew_pt, rh, press,

vis, wind_min, wind_max, wind_avg,

wind_to_dir, wnd_eward, wnd_nthward

from marine_weather_stations s, weather_daily d

where d.stnid=s.stnid;

### Weekly averages from joined tables

select s.stnid, station, longitude AS "lon", latitude AS "lat", elevation_m AS "ht",

stnid, datetime, epoch, temp, dew_point, rel_hum_pc, wind_dir_10s, wind,

visibility, press, humidity, wind_chill, weather, geom

from marine_weather_stations s, weather_hourly h

where d.stnid=s.stnid;

# CITIZEN SCIENCE TABLES

## Drop existing table and create new

DROP TABLE IF EXISTS \<tablename\>;CREATE TABLE citsci_stations (

gid integer,

Line varchar(12),

crew varchar(10),

datetime timestamptz,

epoch integer,

station varchar(12),

long numeric(10,3),

lat numeric(10,3),

x_albers numeric(10,1),

y_albers numeric(10,1),

dist_kms numeric(10,3),

tdist_mins numeric(10,3),

Log_Man varchar(12),

depth_min numeric(7,1),

depth_max numeric(7,1),

date date,

time time,

castid varchar(25)

);

## Load table from csv, add geometry column from lat/long

\COPY citsci_stations ./CitSciCastInfo_20180417.csv CSV HEADER;

SELECT AddGeometryColumn ('data','citsci_stations','geom',4326,'POINT',2);

UPDATE table SET geom = ST_SetSRID(ST_MakePoint(long, lat), 4326);

# WEATHER TABLES

Name climateID longitude latitude timestamp Temp_degC Temp_Flag Dew_Point_degC Dew_Point_Flag Rel_Hum_pc Rel_Hum_Flag Wind_Dir_10s_deg Wind_Dir_Flag Wind_Spd_kmh Wind_Spd_Flag Visibility_km Visibility_Flag Press_kPa Press_Flag Hmdx Hmdx_Flag Wind_Chill Wind_Chill_Flag Weather

## DROP TABLE IF EXISTS, Create table

DROP TABLE IF EXISTS weather_hourly;

CREATE TABLE weather_hourly (

Name varchar(30),

climateID varchar(15),

longitude numeric(7,2),

latitude numeric(7,2),

timestamp timestamp with time zone,

Temp_degC numeric(5,1),

Temp_Flag varchar(5),

Dew_Point_degC numeric(5,1),

Dew_Point_Flag varchar(5),

Rel_Hum_pc numeric(5,1),

Rel_Hum_Flag varchar(5),

Wind_Dir_10s_deg smallint,

Wind_Dir_Flag varchar(5),

Wind_Spd_kmh smallint,

Wind_Spd_Flag varchar(5),

Visibility_km numeric(5,1),

Visibility_Flag varchar(5),

Press_kPa numeric(5,1),

Press_Flag varchar(5),

Hmdx smallint,

Hmdx_Flag varchar(5),

Wind_Chill numeric(5,1),

Wind_Chill_Flag varchar(5),

Weather varchar(100)

);

## DROP TABLE IF EXISTS, Create table

DROP TABLE IF EXISTS weather_daily2;

CREATE TABLE weather_daily2 AS

select climateid,name,longitude,latitude,

timestamp::date AS "date",

AVG(temp_degC)::numeric(7,2) AS "temp",stddev(temp_degC)::numeric(5,1) AS "temp_sd",

AVG(dew_point_degC)::numeric(5,1) AS "dew_pt", AVG(rel_hum_pc)::numeric(5,1) AS "rh",

AVG(press_kpa)::numeric(5,1) AS "press",stddev(press_kpa)::numeric(5,1) AS "p_sd",

AVG(visibility_km)::numeric(7,1) AS "vis",

min(wind_spd_kmh) AS "wind_min",max(wind_spd_kmh) AS "wind_max",

SQRT(POWER(AVG(-wind_spd_kmh\*COS(RADIANS(wind_dir_10s_deg \* 10 ) ) ),2 ) +

POWER(AVG(-wind_spd_kmh\*SIN(RADIANS(wind_dir_10s_deg \* 10 ) ) ),2 ) )::numeric(7,1) AS "wind_avg",

90 - DEGREES(ATAN2(AVG(-wind_spd_kmh\*COS(RADIANS(wind_dir_10s_deg \* 10 ))),

AVG(-wind_spd_kmh\*SIN(RADIANS(wind_dir_10s_deg \* 10 )))) )::numeric(7,1) AS "wind_to_dir",

AVG(-wind_spd_kmh\*SIN(RADIANS(wind_dir_10s_deg \* 10 ) ) )::numeric(7,1) AS "wnd_eward",

AVG(-wind_spd_kmh\*COS(RADIANS(wind_dir_10s_deg \* 10 ) ) )::numeric(7,1) AS "wnd_nthward"

from weather_hourly2

group by climateid,name,longitude,latitude,date;

# FORAGE FISH TABLES

## Create forage fish table

CREATE TABLE data.foragefish_rll_it_cmn_pss (

station character varying,

lat numeric(12,5),

long numeric(12,5),

observation_date date,

sampling_time time without time zone,

species_sampled character varying,

site_sample_number character varying,

sample_type character varying,

sed_primary character varying,

sed_sec_1 character varying,

sed_sec_2 character varying,

shading character varying,

vegetation character varying,

foreshore_mod character varying,

foreshore_structure character varying,

foreshore_landuse character varying,

backshore_mod character varying,

backshore_structure character varying,

backshore_landuse character varying,

tidal_land_mark character varying,

distance_from_landmark numeric(10,3),

beach_slope character varying,

calculated_tidal_elevation numeric(10,3),

width_of_zone character varying,

length_avail_habitat character varying,

sample_volume character varying,

spawn_density character varying,

spawn_present character varying,

comment_general character varying,

comment_sediment character varying,

time_start time without time zone,

time_end time without time zone,

landmass character varying,

municipality character varying,

location character varying,

gps_unit character varying,

weather_conditions character varying,

air_temp numeric(10,1),

beach_aspect character varying,

compass_direction_beach_faces character varying,

reference_tide_height character varying,

last_high_tide_height character varying,

tide_height_at_time_start numeric(10,3),

exposure character varying,

fetch1 character varying,

phyident character varying,

transect character varying,

sed_date_processed date,

sediment_appearance character varying,

number_eggs character varying,

comment_eggs character varying,

organization character varying,

primary_field_surveyor character varying,

sed_processor character varying,

data_entry character varying,

objectid character varying,

sed_continuity character varying,

grain_size character varying,

sed_depth character varying,

neg_sed character varying,

habitat character varying,

anthro character varying,

geom2 public.geometry(MultiLineString,3005),

gid integer NOT NULL

);

# PIT TAG DETECTION TABLES

## Very fast query to sort pit detections for 

dups and uniques (to get all uniques, omit WHERE row \> 1 OR nextrow \> 1)

\# explain analyze

SELECT \*

FROM (

SELECT \*, LEAD(row,1) OVER () AS nextrow

FROM (

SELECT \*, ROW_NUMBER() OVER(w) AS row

FROM det_fme

WINDOW w AS

( PARTITION BY tagid, datetime ORDER BY location)

) x

) y

WHERE row \> 1 OR nextrow \> 1

;

QUERY PLAN

Subquery Scan on y (cost=552192.66..688588.02 rows=1262920 width=118) (actual time=13185.555..21204.516 rows=1821959 loops=1)

Filter: ((y."row" \> 1) OR (y.nextrow \> 1))

Rows Removed by Filter: 350005

-\> WindowAgg (cost=552192.66..654489.18 rows=2273256 width=118) (actual time=13185.551..20803.065 rows=2171964 loops=1)

-\> WindowAgg (cost=552192.66..603340.92 rows=2273256 width=110) (actual time=13185.533..18250.051 rows=2171964 loops=1)

-\> Sort (cost=552192.66..557875.80 rows=2273256 width=102) (actual time=13185.492..15712.167 rows=2171964 loops=1)

Sort Key: det_fme.tagid, det_fme.datetime, det_fme.location

Sort Method: external merge Disk: 263640kB

-\> Seq Scan on det_fme (cost=0.00..63538.56 rows=2273256 width=102) (actual time=739.366..1898.564 rows=2171964 loops=1)

Planning Time: 0.202 ms

JIT:

Functions: 12

Options: Inlining true, Optimization true, Expressions true, Deforming true

Timing: Generation 25.859 ms, Inlining 52.403 ms, Optimization 414.265 ms, Emission 266.696 ms, Total 759.224 ms

Execution Time: 21485.836 ms

(15 rows)

CREATE TABLE det_grouped_tag_dt_loc AS (

SELECT

tagid, count(distinct(fname)) AS "numFiles", count(\*) AS "numLocDetsAll",

count(distinct(right(fname,2))) AS "distinctLocDets", array_agg(distinct(right(fname,2))) "distinctLocs",

min(datetime) AS "start_time",max(datetime) AS "stop_time",

(extract(epoch from (max(datetime)-min(datetime)) )/86400)::numeric(10,2) AS duration_days,

STRING_AGG(distinct(fname), ';') "fnamesDistinct_NotInSequence"

FROM det_unique

GROUP BY tagid

ORDER BY "distinctLocDets" DESC,"distinctLocs",start_time

);
