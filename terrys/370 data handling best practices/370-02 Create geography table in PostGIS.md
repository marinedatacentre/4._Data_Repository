---
title: "370-02 Create geography table in PostGIS"
source_file: "C:\Users\tchernen\handbook_docx\4_Data_Repository\terrys\370 data handling best practices\370-02 Create geography table in PostGIS.docx"
review_period: "3 years"
created_by: "Peter"
---

**Purpose:**

This document describes how to create a geography table (cf more common geometry table) and add CSV data to PostGIS.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 50%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Step</strong></th>
<th style="text-align: left;"><strong>Major Activity</strong></th>
<th><blockquote>
<p><strong>References, Forms and Details</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: left;"><p>CREATE TABLE &lt;table&gt; (</p>
<p>&lt;gid&gt; PRIMARY KEY,</p>
<p>Varname type,</p>
<p>* * *</p>
<p>geog geography (POINT, 4326)</p>
<p>) ;</p></td>
<td><ul>
<li><p>Replace &lt;table&gt; with a user-chosen table name, and &lt;gid&gt; with column with unique values</p></li>
<li><p>Geography column must be named geog to work with QGIS</p></li>
<li><p>Only 4326 ‘projection’ supported</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: left;"><ul>
<li><p>Create a CSV file with a column containing POINT(longitude1 latitude1)</p></li>
<li><p>Transfer to PostGIS server</p></li>
</ul></td>
<td><ul>
<li><p>Note the space delimiter, not a comma</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: left;"><ul>
<li><p>In psql,</p></li>
</ul>
<blockquote>
<p>\COPY &lt;table&gt; FROM path/filename.ext DELIMITERS ‘,’ CSV HEADER;</p>
</blockquote></td>
<td><ul>
<li><p>File must be on the server</p></li>
<li><p>Assumes the CSV file delimiter is a comma</p></li>
<li><p>If no header, delete that keyword</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: left;"><ul>
<li><p>CREATE INDEX &lt;column_name&gt;_idx ON &lt;table&gt; (&lt;column_name&gt;);</p></li>
</ul></td>
<td><ul>
<li><p>Index can be named anything meaningful and unique</p></li>
<li><p>Replace &lt;…&gt; with the appropriate names</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: left;"><p>Create a spatial index:</p>
<p>CREATE INDEX &lt;table_name&gt;_gix</p>
<p>ON &lt;table_name&gt; USING GIST(geog);</p></td>
<td><ul>
<li><p>Column should be named ‘geog’ to work properly with QGIS</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: left;"><p>In psql, \d &lt;table_name&gt;</p>
<p>to observe columns and index(es) appropriately named and created</p></td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: left;"><p>Issue a SELECT* FROM &lt;table&gt; LIMIT 5;</p>
<p>To check data is loaded</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td style="text-align: left;"><p>Issue a SELECT COUNT(*) FROM &lt;table&gt;;</p>
<p>To ensure all data was loaded</p></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>
