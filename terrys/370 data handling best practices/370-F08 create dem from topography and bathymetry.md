---
title: "370-F08 create dem from topography and bathymetry"
source_file: "C:\Users\tchernen\handbook_docx\4_Data_Repository\terrys\370 data handling best practices\370-F08 create dem from topography and bathymetry.docx"
review_period: "3 years"
created_by: "Peter"
---

**Purpose:**

This document describes how to create a digital terrain model (dem) from topography and non-navigation bathymetry downloaded form the open.canada.ca website.

Although the datsets are each available as tiles in zipped tiff format, they are handled separately. Past attempts at simply joining the two data types have proven unsuccessful. This is because the vertical reference for topography is mean sea level, while the bathymetry is on chart datum, which means that each tiff is potentially on a different vertical datum, and generally on a datum related to lower low water large tides.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 55%" />
<col style="width: 31%" />
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
<td style="text-align: left;"><p>Download the 250K topography from the cdem</p>
<ul>
<li><p><a href="https://open.canada.ca/data/en/dataset/7f245e4d-76c2-4caa-951a-45d1d2051333"><u>https://open.canada.ca/data/en/dataset/7f245e4d-76c2-4caa-951a-45d1d2051333</u></a></p></li>
<li><p>download all geotiffs in the 92, 93, 102 and 103</p></li>
</ul></td>
<td><ul>
<li><p>The fastest approach is to use fileftp, and change the “https” to “ftp”</p></li>
<li><p>point spacing is 0.75 arc secs (about 20 metres)</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: left;">Unzip the tiffs</td>
<td><ul>
<li><p>This can be done easily in Linux, and not so easily in Windows</p></li>
<li><p>unzip ‘*.zip’</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: left;"><p>Convert the topography geotiffs to xyz</p>
<ul>
<li><p>gdal_translate -of XYZ &lt;geotiff name&gt; &lt;geotiff name&gt;.xyz</p></li>
<li><p>replace values of « 0 » and « ~1E38 » with a known null value</p></li>
</ul></td>
<td><ul>
<li><p>With this approach, you have a file extension “.tif.xyz” which does not matter</p></li>
<li><p>the XYZ files total about 50GB</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: left;"><p>Download the zipped-tif format file of 100m nonnav bathymetry</p>
<ul>
<li><p><a href="https://open.canada.ca/data/en/dataset/d3881c4c-650d-4070-bf9b-1e00aabf0a1d"><u>https://open.canada.ca/data/en/dataset/d3881c4c-650d-4070-bf9b-1e00aabf0a1d</u></a></p></li>
</ul></td>
<td><ul>
<li><p>It is a single 150MB download, containing bathymetry for all of Canada including the Arctic, but not US waters.</p></li>
<li><p>Point spacing is 0.001 arc seconds (~111 metres)</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: left;">Unzip the single zip file</td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: left;">Convert the geotiffs to XYZ</td>
<td><ul>
<li><p>Same approach as above</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: left;">Optional. Alter the bathymetry to mean sea level</td>
<td><ul>
<li><p>If this is not done, the final dem depths will be somewhat in error (up to 5 metres).</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td style="text-align: left;"><p>Grid the resulting datasets as one</p>
<ul>
<li><p>modified xyz topography</p></li>
<li><p>bathymetry xyz files</p></li>
<li><p>any supplemental bathymetry files in xyz</p></li>
</ul></td>
<td><ul>
<li><p>Need a gridding application that can handle very large datsets.</p></li>
<li><p>one can specify a cell size as 0.0005 deg (~50metres)</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">9</td>
<td style="text-align: left;"></td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">10</td>
<td style="text-align: left;"></td>
<td><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>
