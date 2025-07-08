**Purpose:**

This document describes how to add CSV data to PostGIS located on a remote computer using the Linux operating system, for subsequent use as a spatial layer in GeoServer. Data is often organized as a table, and CSV is a useful exchange format. An alternative is to create the file in shape format, and load that.

The version of Linux used was CentOS, which is a non-graphical interface. Thus, the process should work for virtually all operating systems. The description incudes the process of first passing data to a remote computer. The processes were adapted from descriptions on the web.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 53%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Step</strong></th>
<th style="text-align: left;"><strong>Major Activity</strong></th>
<th style="text-align: left;"><strong>References, Forms and Details</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: left;"><p>Pass the file to the remote computer. In Linux, this is:</p>
<ul>
<li><p>$ scp foobar.txt</p></li>
</ul>
<p><a href="mailto:your_username@remotehost.edu:/some/remote/directory">your_username@remotehost.edu:/some/remote/directory</a></p>
<p>To pass multiple files in a single step:</p>
<ul>
<li><p>$ scp foo.txt bar.txt <a href="mailto:your_username@remotehost.edu:~">your_username@remotehost.edu:~</a></p></li>
</ul></td>
<td style="text-align: left;"><p>Other file-moving variants are mentioned at:</p>
<p><a href="http://www.hypexr.org/linux_scp_help.php">http://www.hypexr.org/linux_scp_help.php</a></p></td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: left;"><p>Log onto the remote computer</p>
<ul>
<li><p>ssh –t &lt;username&gt;@remotehost.edu</p></li>
</ul></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: left;"><p>Move to the location of the CSV file(s)</p>
<ul>
<li><p>cd /some/remote/directory</p></li>
</ul></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: left;"><p>Create an empty table in PostGIS</p>
<ul>
<li><p>psql &lt;database &lt;username&gt;</p></li>
<li><p>DROP TABLE IF EXISTS &lt;tablename&gt;;</p></li>
<li><p>CREATE TABLE &lt;tablename&gt; (</p></li>
</ul>
<blockquote>
<p>Col_1_name &lt;data_type&gt;,</p>
<p>Col_2_name &lt;data_type&gt;,</p>
<p>. . .</p>
<p>Col_n_name &lt;data_type&gt;</p>
<p><mark></mark></p>
<p>);</p>
</blockquote></td>
<td style="text-align: left;"><ul>
<li><p>Note opening and closing parentheses for create table</p></li>
<li><p>Common numeric and character types:</p>
<ul>
<li><p>The <strong>real</strong> type typically has a range of at least 1E-37 to 1E+37 with a precision of at least 6 decimal digits.</p></li>
<li><p>The <strong>double precision</strong> type typically has a range of around 1E-307 to 1E+308 with a precision of at least 15 digits.</p></li>
<li><p>The type <strong>integer</strong> is a common choice, as it offers the best balance between range, storage size, and performance.</p></li>
<li><p>The notations <strong>varchar(n)</strong> and <strong>char(n)</strong> are aliases for <strong>character varying(n)</strong> and <strong>character(n),</strong> respectively. <strong>character</strong> without length specifier is equivalent to character(1).</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: left;"><p>If planning to load a geometry string as text, then prefix the point, line or multiline string with:</p>
<blockquote>
<p>SRID=&lt;epsg code&gt;; &lt;string&gt;</p>
</blockquote></td>
<td style="text-align: left;"><ul>
<li><p>Allows point, line or multiline string to include the epsg code and load</p></li>
<li><p>note the semi-colon before the &lt;string&gt;</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: left;"><p>Still in psql, and if the file has a header:</p>
<p>\COPY &lt;tablename&gt; FROM '/path/to/filename.csv'</p>
<p>DELIMITER ',' CSV HEADER;</p></td>
<td style="text-align: left;"><ul>
<li><p>If no header, omit the HEADER attribute</p></li>
<li><p>Use \copy (and not simply copy) because one does not need special privileges to perform.</p></li>
<li><p>If space-delimited data, use ‘ ‘</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: left;"><p>Add a numerical column for primary key:</p>
<p>ALTER TABLE &lt;tablename&gt; ADD COLUMN gid serial PRIMARY KEY;</p></td>
<td style="text-align: left;"><ul>
<li><p>Creates a binary tree search index</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td style="text-align: left;"><p>Create a geometry column:</p>
<p>SELECT <strong>AddGeometryColumn</strong>(‘<em>schema_name’</em>, ‘<em>spatial table_name’</em>, <em>‘geom</em>’, srid, ‘<em>type’</em>, <em>dimension</em>);</p></td>
<td style="text-align: left;"><ul>
<li><p>Example:</p></li>
</ul>
<p>SELECT AddGeometryColumn ('data','placenames','geom' ,3005,'POINT',2);</p>
<ul>
<li><p>srid = 4326 (latitude, longitude on datum WGS84), etc (no quotes)</p></li>
<li><p>type=POINT, etc</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">98</td>
<td style="text-align: left;"><p>Update the geometry column:</p>
<p>UPDATE &lt;tablename&gt;</p>
<p>SET geom = ST_SetSRID(ST_MakePoint(longitude,latitude),4326);</p></td>
<td style="text-align: left;"><ul>
<li><p>This could identify a projected coordinate system, for instance, an UTM projection with northings and eastings.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">10</td>
<td style="text-align: left;"><p>Create a spatial index:</p>
<p>CREATE INDEX &lt;suitable_name&gt;_geom_idx</p>
<p>ON &lt;tablename&gt; USING GIST(geom);</p></td>
<td style="text-align: left;"><ul>
<li><p>The index name is a free choice, but should be meaningful</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">110</td>
<td style="text-align: left;">Check tble permission for geoserver application access</td>
<td style="text-align: left;"><ul>
<li></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">12</td>
<td style="text-align: left;"><p>Test for correctness</p>
<p>\d &lt;tablename&gt;</p></td>
<td style="text-align: left;"><ul>
<li><p>Should see serial PKey and GIST index, as well as columns</p></li>
</ul></td>
</tr>
</tbody>
</table>
