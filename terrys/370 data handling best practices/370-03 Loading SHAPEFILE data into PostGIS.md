**Purpose:**

This document describes how to add Shapefile data to PostGIS located on a remote computer using the Linux operating system, for subsequent use as a spatial layer in GeoServer. Data is often organized as a table, and shapefile is often regarded as the easiest format for data exchange. An alternative is to create the file in CSV format, and load that.

PostGIS includes the shp2pgsql tool for converting shapefiles into database tables. This document describes how to use this tool to load a single or multiple shapefiles.

shp2pgsql converts a shapefile into a series of SQL commands that can be loaded into a database–it does **not** perform the actual loading. The output of this command may be captured in a SQL file, or piped directly to the psql command, which will execute the commands against a target database.

The following process is taken fairly directly from: <http://suite.opengeo.org/4.1/dataadmin/pgGettingStarted/shp2pgsql.html>)

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 54%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Step</strong></th>
<th style="text-align: left;"><strong>Major Activity</strong></th>
<th><strong>References, Forms and Details</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: left;">Select the shapefile you wish to load—you will need all the files: .shp, .shx, and .dbf and so on.</td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: left;"><p>Identify the SRID (“projection”) of your data.</p>
<ul>
<li><p>If available, this information is easily accessed via the layer metadata in GeoServer.</p></li>
<li><p>If the projection is unknown, use a service like <a href="http://prj2epsg.org/"><u>prj2epsg.org</u></a> to upload and convert the shapefile’s .prj file to a SRID code.</p></li>
</ul></td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: left;">Either identify the target database where you would like to load the data, or create a new database</td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: left;"><p>Confirm PostGIS is responding to requests by executing the following psql query:</p>
<p>psql -c "SELECT PostGIS_Version()"</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: center;">5a</td>
<td style="text-align: left;"><p><strong><u>Do either step 5a or step 5b</u></strong></p>
<p>Run the shp2pgsql command and pipe the output into the psql command to load the shapefile into the database in one step. The recommended syntax is:</p>
<p>shp2pgsql -I -s &lt;SRID&gt; &lt;PATH/TO/SHAPEFILE&gt; &lt;SCHEMA&gt;.&lt;DBTABLE&gt; | psql -d &lt;DATABASE&gt; -U postgres</p>
<p><u>example:</u></p>
<p>shp2pgsql -I -s 4269 C:\MyData\roads\roads.shp roads | sudo -u postgres psql -d MyDatabase</p>
<p>The -I option will create a spatial index after the table is created. This is strongly recommended for improved performance.</p>
<p>The -s option indicates the SRID follows.</p></td>
<td><p>The command parameters are:</p>
<ul>
<li><p>&lt;SRID&gt;—Spatial reference identifier</p></li>
<li><p>&lt;PATH/TO/SHAPEFILE&gt;—Full path to the shapefile (such as C:\MyData\roads\roads.shp)</p></li>
<li><p>&lt;SCHEMA&gt;—Target schema where the new table will be created</p></li>
<li><p>&lt;DBTABLE&gt;—New database table to be created (usually the same name as the source shapefile)</p></li>
<li><p>&lt;DATABASE&gt;—Target database where the table will be created</p></li>
</ul>
<blockquote>
<p>For more information about shp2pgsql command options, please refer to 305-F03.</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;">5b</td>
<td style="text-align: left;"><p>If you want to capture the SQL commands, pipe the output to a file:</p>
<p>shp2pgsql -I -s &lt;SRID&gt; &lt;PATH/TO/SHAPEFILE&gt; &lt;DBTABLE&gt; &gt; SHAPEFILE.sql</p>
<p>The file can be loaded into the database later by executing the following:</p>
<p>psql -d &lt;DATABASE&gt; -f SHAPEFILE.sql</p></td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: left;"><p>Confirm the shapefile has now been imported as a table in your PostGIS database. You can verify this by either using pgAdmin to view the list of tables, or by executing the following query at the command line:</p>
<p>psql -U &lt;USERNAME&gt; -d &lt;DATABASE&gt; -c "\d"</p></td>
<td><ul>
<li><p>If not, redo</p></li>
</ul></td>
</tr>
</tbody>
</table>
