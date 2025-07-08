**Purpose:**

This document describes the production of data files for inclusion in a geospatial data management system. The intent is to have a documented and traceable list of changes that can be examined by others. This lineage process results in version control, lack of ambiguity, confidence in the resulting product, and is consistent with international metadata documentation.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 37%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>Step</strong></th>
<th style="text-align: left;"><strong>Major Activity</strong></th>
<th style="text-align: left;"><strong>References, Forms and Details</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">1</td>
<td style="text-align: left;"><p>Acquire the dataset</p>
<ul>
<li><p>note the receipt date</p></li>
<li><p>determine if changes are needed</p></li>
<li><p>notify the upstream data provider of the intended changes, and rationale</p></li>
</ul></td>
<td style="text-align: left;"><p>The following data precision can be truncated <u>from the right</u>, if full precision is not needed:</p>
<ul>
<li><p>dates as yyyy-mm-dd</p></li>
<li><p>times (if needed) as hh:mm:ss</p></li>
<li><p>time zone as PDT, PST, Z (UTC), or +/-07</p></li>
<li><p>if point data, latitudes and longitudes as +/- ddd.ddddd (five decimals, ~1m at equator)</p></li>
<li><p>if polygon data (e.g. PFMA or NPAFC), identify where the polygon definitions may be found.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;">2</td>
<td style="text-align: left;"><p>Perform and document the changes</p>
<ul>
<li><p>date (and time if appropriate) of the change</p></li>
<li><p>name processor, affiliation and email address</p></li>
<li><p>brief description of the changes</p></li>
<li><p>rationale</p></li>
</ul></td>
<td style="text-align: left;">If the changes involved reference to an industry standard, the source should be noted.</td>
</tr>
<tr>
<td style="text-align: left;">3</td>
<td style="text-align: left;"><p>Create the data output format as:</p>
<ul>
<li><p>comma-separated values (CSV),</p></li>
<li><p>workbook format (xlsx, openDoc)</p></li>
<li><p>shapefile(s)</p></li>
</ul></td>
<td style="text-align: left;"><p>The CSV file can be any separator, providing there is no ambiguity – for example, spaces or tabs are acceptable.</p>
<p>PDF documents are only acceptable as accompanying documents, because changes are difficult.</p></td>
</tr>
<tr>
<td style="text-align: left;">4</td>
<td style="text-align: left;">Forward the output data products to the data centre, copy to the upstream data provider.</td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>
