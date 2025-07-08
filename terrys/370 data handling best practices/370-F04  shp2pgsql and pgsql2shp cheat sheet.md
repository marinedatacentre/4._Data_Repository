---
title: "370-F04  shp2pgsql and pgsql2shp cheat sheet"
source_file: "C:\Users\tchernen\handbook_docx\4_Data_Repository\terrys\370 data handling best practices\370-F04  shp2pgsql and pgsql2shp cheat sheet.docx"
review_period: "3 years"
created_by: "Terry Curran"
created: "2018-12-11"
modified: "2019-09-10"
---

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>PostGIS 2.0.0 pgsql2shp shp2pgsql Cheat Sheet 340-F04</strong></p>
<p><strong>2018-Dec-10</strong></p>
<p>(from <a href="http://bostongis.com/pgsql2shp_shp2pgsql_quickguide.bqg">http://bostongis.com/pgsql2shp_shp2pgsql_quickguide.bqg</a> )</p>
<p>shp2pgsql and pgsql2shp are all located in the bin folder of the PostgreSQL install.</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><strong><mark>pgsql2shp dumps a postgis database table, view or sql query to ESRI shape file format.</mark></strong></p>
<p><strong>USAGE:</strong> pgsql2shp [OPTIONS] database [schema.]table pgsql2shp [OPTIONS] <em>database</em> <em>query</em></p></td>
</tr>
<tr>
<td><p><strong><mark>shp2pgsql generates an SQL script from ESRI shape and DBF files suitable for loading into a PostGIS enabled database.</mark></strong></p>
<p><strong>USAGE:</strong> shp2pgsql [<em>OPTIONS</em>] <em>shapefile</em> [<em>schema.</em>]<em>table</em></p></td>
</tr>
<tr>
<td><p>New in 2.0.0 <sup>1</sup>, New in 1.5<sup>2</sup></p>
<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 26%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr>
<th colspan="3"><strong><mark>General options: (P - pgsql2shp, S - shp2pgsql)</mark></strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>P</p>
<p>S</p>
<p>S</p>
<p>S</p>
<p>S</p>
<p>S</p>
<p>S</p>
<p>P</p>
<p>P S</p>
<p>P</p>
<p>S</p>
<p>S</p>
<p>P S</p>
<p>S</p>
<p>S</p>
<p>S</p>
<p>P</p>
<p>P</p>
<p>P</p>
<p>S</p>
<p>P</p>
<p>S</p>
<p>S</p>
<p>S</p>
<p>S</p>
<p>S</p>
<p>S</p>
<p>S</p>
<p>P</p>
<p>P S</p></td>
<td><p>-b</p>
<p>-s <em>from_srid:to_srid</em></p>
<p>(-d|a|c|p)</p>
<p>-d</p>
<p>-a</p>
<p>-c</p>
<p>-p</p>
<p>-f <em>filename</em></p>
<p>-g <em>geometry_column_name</em></p>
<p>-h <em>hostname</em></p>
<p>-D</p>
<p>-e</p>
<p>-k</p>
<p>-i</p>
<p>-I</p>
<p>-p <em>port</em></p>
<p>-P <em>password</em></p>
<p>-r</p>
<p>-S</p>
<p>-u <em>user</em></p>
<p><em>-w</em></p>
<p><em>-W</em></p>
<p><em>-N</em></p>
<p><em>-n</em></p>
<p><em>-G<sup>2</sup></em></p>
<p><em>-T<sup>1</sup></em></p>
<p><em>-X<sup>1</sup></em></p>
<p><em>-m<sup>1</sup> filename</em></p>
<p><em>-?</em></p></td>
<td><p>Use a binary cursor.</p>
<p>If -s :to_srid <sup>1</sup> is not specified then from_srid is assumed and no transformation happens.</p>
<p>These are mutually exclusive options:</p>
<p>Drops the table, then recreates it and populates it with current shape file data.</p>
<p>Appends shape file into current table, must be exactly the same table schema.</p>
<p>Creates a new table and populates it, default if you do not specify any options.</p>
<p>Prepare mode, only creates the table.</p>
<p>Use this option to specify the name of the file to create</p>
<p>Specify the name of the geometry column to be (S) created (P) exported.</p>
<p>Specify db server host name defaults to localhost.</p>
<p>Use postgresql dump format (defaults to sql insert statments).</p>
<p>Execute each statement individually, do not use a transaction. Not compatible with -D</p>
<p>Keep postgresql identifiers case.</p>
<p>Use int4 type for all integer dbf fields.</p>
<p>Create a GiST index on the geometry column.</p>
<p>Allows you to specify a database port other than the default. Defaults to 5432.</p>
<p>Connect to the database with the specified password.</p>
<p>Raw mode. Do not unescape attribute names and not skip the 'gid' attribute.</p>
<p>Generate simple geometries instead of MULTI geometries.</p>
<p>Connect to the database as the specified user.</p>
<p>Use wkt format (for postgis-0.x support - drops M - drifts coordinates).</p>
<p><em>encoding</em> The character encoding of Shape's attribute column. (default : "UTF-8")</p>
<p><em>policy</em> Specify NULL geometries handling policy (insert,skip,abort)</p>
<p>Only import DBF file.</p>
<p>Use geography type instead of geometry (requires lon/lat data) in WGS84 long lat (-s SRID=4326)</p>
<p>Specify the tablespace for the new table. Indexes will still use the default tablespace unless the -X parameter is also used.</p>
<p>Specify the tablespace for the new index.</p>
<p>Remap identifiers to ten character names. The content of the file is lines of two symbols separated by a single white space.</p>
<p>Display this help screen</p></td>
</tr>
<tr>
<td colspan="3"><p><strong><mark>PSQL Connection options:</mark></strong></p>
<p>-h, --host=HOSTNAME database server host or socket directory</p>
<p>-p, --port=PORT database server port number</p>
<p>-U, --username=NAME connect as specified database user</p>
<p>-W, --password force password prompt (should happen automatically)</p>
<p>-e, --exit-on-error exit on error, default is to continue</p>
<p>If no input file name is supplied, then standard input is used.</p></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong><mark>Loading data with shp2pgsql</mark></strong></p>
<p><mark>Load data into PostgreSQL from ESRI shape file MA stateplane feet</mark></p>
<p>shp2pgsql -s 2249 neighborhoods public.neighborhoods &gt; neighborhoods.sql</p>
<p>psql -h myserver -d mydb -U myuser -f neighborhoods.sql</p>
<p><mark>Do above in one step</mark></p>
<p>shp2pgsql -s 4326 neighborhoods public.neighborhoods | psql -h myserver -d mydb -U myuser</p>
<p><mark>Load data into PostgreSQL from ESRI shape file MA stateplane feet to geography</mark></p>
<p>shp2pgsql -G -s 2249:4326 neighborhoods public.neighborhoods &gt; neighborhoods_geog.sql</p>
<p>psql -h myserver -d mydb -U myuser -f neighborhoods_geog.sql</p>
<p><mark>Sample linux sh script to load tiger 2007 massachusetts edges and landmark points</mark></p>
<p>TMPDIR="/gis_data/staging"</p>
<p>STATEDIR="/gis_data/25_MASSACHUSETTS"</p>
<p>STATESCHEMA="ma"</p>
<p>DB="tiger"</p>
<p>USER_NAME="tigeruser"</p>
<p>cd $STATEDIR</p>
<p>#unzip files into temp directory</p>
<p>for z in */*.zip; do unzip -o -d $TMPDIR $z; done</p>
<p>for z in *.zip; do unzip -o -d $TMPDIR $z; done</p>
<p>#prepare the tables don't load data</p>
<p>#force non-multi and set the geometry column name to the_geom_4269, dbf is in latin1 encoding</p>
<p>shp2pgsql -s 4269 -g the_geom_4269 -S -W "latin1" -p fe_2007_25025_edges.shp ${STATESCHEMA}.edges | psql -U $USER_NAME -d $DB</p>
<p>shp2pgsql -s 4269 -g the_geom_4269 -S -W "latin1" -p fe_2007_25025_pointlm.shp ${STATESCHEMA}.pointlm | psql -U $USER_NAME -d $DB</p>
<p>#loop thru pointlm and edges county tables and append to respective ma.pointlm ma.edges tables</p>
<p>for t in pointlm edges;</p>
<p>do</p>
<p>for z in *${t}.dbf;</p>
<p>do</p>
<p>shp2pgsql -s 4269 -g the_geom_4269 -S -W "latin1" -a $z ${STATE_SCHEMA}.${t} | psql -d $DB -U $USER_NAME;</p>
<p>done</p>
<p>done</p></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><strong><mark>Outputing to ESRI Shapefile/DBF with pgsql2shp</mark></strong></p>
<p><mark>Export query to a shape file called jpnei.shp/dbf</mark></p>
<p>pgsql2shp -f "/path/to/jpnei" -h myserver -u apguser -P apgpassword mygisdb</p>
<p>"SELECT neigh_name, the_geom FROM neighborhoods WHERE neigh_name = 'Jamaica Plain'"</p>
<p><mark>Export a table in ma schema called streets to streets.shp/dbf</mark></p>
<p>pgsql2shp -f "/path/to/streets" -h myserver -u apguser -P apgpassword mygisdb ma.streets</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>
