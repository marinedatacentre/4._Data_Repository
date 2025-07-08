---
process_number: 370-F03
title: Useful Metadata Snippets
author: Terry Curran
created: 2021-01-26
modified: 2021-01-26
review_period: 3 years
---

340-F03

Useful snippets in metadata

**<u>Data Quality</u>**

***explanation* (**missing, unknown, withheld, inapplicable, template)

\</gmd:specification\>

\<gmd:explanation gco:nilReason="missing" /\>

\<gmd:pass\>

***Missing DQ code list value***

> codeListValue="indirect"

**<u>Dates</u>** (see NOAA list for more date formats)

***Unknown***

\<gmd:date gco:nilReason="unknown" /\>

***For single time***

\<gml:TimeInstant gml:id="d1e50"\>

\<gml:timePosition\>2003-01-18T00:23:00.000Z\</gml:timePosition\>

\</gml:TimeInstant\>

**<u>Vertical Reference</u>**

***If unknown,***

\<gmd:verticalCRS gco:nilReason="unknown"/\>

***Some other (non-inclusive) options:***

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 7%" />
<col style="width: 39%" />
<col style="width: 15%" />
<col style="width: 7%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr>
<th><strong>Name</strong></th>
<th><strong>Alias</strong></th>
<th><strong>EPSG code</strong></th>
<th><strong>Area</strong></th>
<th><strong>Remarks</strong></th>
<th><strong>Units</strong></th>
<th><strong>Dir’n</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><table>
<colgroup>
<col style="width: 0%" />
<col style="width: 99%" />
</colgroup>
<thead>
<tr>
<th></th>
<th>CGVD2013 height</th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td><table>
<colgroup>
<col style="width: 0%" />
<col style="width: 99%" />
</colgroup>
<thead>
<tr>
<th></th>
<th>Canadian Geodetic Vertical Datum of 2013 height</th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td>6647</td>
<td><table>
<colgroup>
<col style="width: 0%" />
<col style="width: 99%" />
</colgroup>
<thead>
<tr>
<th></th>
<th>Canada - onshore and offshore - Alberta; British Columbia; Manitoba; New Brunswick; Newfoundland and Labrador; Northwest Territories; Nova Scotia; Nunavut; Ontario; Prince Edward Island; Quebec; Saskatchewan; Yukon.</th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td>Replaces CGVD28 height (CRS code 5713). CGVD2013 is realized by geoid model CGG2013 (tfm code 6648).</td>
<td>metre</td>
<td>Up</td>
</tr>
<tr>
<td><table>
<colgroup>
<col style="width: 0%" />
<col style="width: 99%" />
</colgroup>
<thead>
<tr>
<th></th>
<th>CGVD28 height</th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td><table>
<colgroup>
<col style="width: 0%" />
<col style="width: 99%" />
</colgroup>
<thead>
<tr>
<th></th>
<th>Canadian Geodetic Vertical Datum of 1928 height</th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td>5713</td>
<td><table>
<colgroup>
<col style="width: 0%" />
<col style="width: 99%" />
</colgroup>
<thead>
<tr>
<th></th>
<th>Canada - onshore - Alberta; British Columbia; Manitoba south of 57°N; New Brunswick; Northwest Territories south west of a line between 60°N, 110°W and the coast at 132°W; Nova Scotia; Ontario south of 52°N; Prince Edward Island; Quebec - mainland west of 66°W and south of 55°N; Saskatchewan south of 55°N; Yukon.</th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td>From November 2013 replaced by CGVD2013 height (CRS code 6647).</td>
<td>metre</td>
<td>Up</td>
</tr>
<tr>
<td><table>
<colgroup>
<col style="width: 0%" />
<col style="width: 99%" />
</colgroup>
<thead>
<tr>
<th></th>
<th>NAVD88 depth</th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td>North American Vertical Datum of 1988 depth (m)</td>
<td>6357</td>
<td>Mexico - onshore. United States (USA) - CONUS and Alaska - onshore - Alabama; Alaska; Arizona; Arkansas; California; Colorado; Connecticut; Delaware; Florida; Georgia; Idaho; Illinois; Indiana; Iowa; Kansas; Kentucky; Louisiana; Maine; Maryland; Massachusetts; Michigan; Minnesota; Mississippi; Missouri; Montana; Nebraska; Nevada; New Hampshire; New Jersey; New Mexico; New York; North Carolina; North Dakota; Ohio; Oklahoma; Oregon; Pennsylvania; Rhode Island; South Carolina; South Dakota; Tennessee; Texas; Utah; Vermont; Virginia; Washington; West Virginia; Wisconsin; Wyoming.</td>
<td></td>
<td>metre</td>
<td>Dn</td>
</tr>
<tr>
<td>NAVD88 depth (ftUS)</td>
<td><table>
<colgroup>
<col style="width: 0%" />
<col style="width: 99%" />
</colgroup>
<thead>
<tr>
<th></th>
<th>North American Vertical Datum of 1988 depth (ftUS)</th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td>6358</td>
<td><table>
<colgroup>
<col style="width: 0%" />
<col style="width: 99%" />
</colgroup>
<thead>
<tr>
<th></th>
<th>United States (USA) - CONUS and Alaska - onshore - Alabama; Alaska mainland; Arizona; Arkansas; California; Colorado; Connecticut; Delaware; Florida; Georgia; Idaho; Illinois; Indiana; Iowa; Kansas; Kentucky; Louisiana; Maine; Maryland; Massachusetts; Michigan; Minnesota; Mississippi; Missouri; Montana; Nebraska; Nevada; New Hampshire; New Jersey; New Mexico; New York; North Carolina; North Dakota; Ohio; Oklahoma; Oregon; Pennsylvania; Rhode Island; South Carolina; South Dakota; Tennessee; Texas; Utah; Vermont; Virginia; Washington; West Virginia; Wisconsin; Wyoming.</th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td><table>
<colgroup>
<col style="width: 0%" />
<col style="width: 99%" />
</colgroup>
<thead>
<tr>
<th></th>
<th>Replaces NGVD29 depth (ftUS) (CRS code 6359).</th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td><table>
<colgroup>
<col style="width: 1%" />
<col style="width: 98%" />
</colgroup>
<thead>
<tr>
<th></th>
<th>US survey foot</th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td>Dn</td>
</tr>
<tr>
<td><table>
<colgroup>
<col style="width: 0%" />
<col style="width: 99%" />
</colgroup>
<thead>
<tr>
<th></th>
<th>NAVD88 height</th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td><table>
<colgroup>
<col style="width: 0%" />
<col style="width: 99%" />
</colgroup>
<thead>
<tr>
<th></th>
<th>North American Vertical Datum of 1988 height (m)</th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td>5703</td>
<td>Mexico - onshore. United States (USA) - CONUS and Alaska - onshore - Alabama; Alaska; Arizona; Arkansas; California; Colorado; Connecticut; Delaware; Florida; Georgia; Idaho; Illinois; Indiana; Iowa; Kansas; Kentucky; Louisiana; Maine; Maryland; Massachusetts; Michigan; Minnesota; Mississippi; Missouri; Montana; Nebraska; Nevada; New Hampshire; New Jersey; New Mexico; New York; North Carolina; North Dakota; Ohio; Oklahoma; Oregon; Pennsylvania; Rhode Island; South Carolina; South Dakota; Tennessee; Texas; Utah; Vermont; Virginia; Washington; West Virginia; Wisconsin; Wyoming.</td>
<td></td>
<td>metre</td>
<td>Up</td>
</tr>
<tr>
<td><table>
<colgroup>
<col style="width: 0%" />
<col style="width: 99%" />
</colgroup>
<thead>
<tr>
<th></th>
<th>NAVD88 height (ftUS</th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td><table>
<colgroup>
<col style="width: 0%" />
<col style="width: 99%" />
</colgroup>
<thead>
<tr>
<th></th>
<th>North American Vertical Datum of 1988 height (ftUS)</th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td>6360</td>
<td>United States (USA) - CONUS and Alaska - onshore - Alabama; Alaska mainland; Arizona; Arkansas; California; Colorado; Connecticut; Delaware; Florida; Georgia; Idaho; Illinois; Indiana; Iowa; Kansas; Kentucky; Louisiana; Maine; Maryland; Massachusetts; Michigan; Minnesota; Mississippi; Missouri; Montana; Nebraska; Nevada; New Hampshire; New Jersey; New Mexico; New York; North Carolina; North Dakota; Ohio; Oklahoma; Oregon; Pennsylvania; Rhode Island; South Carolina; South Dakota; Tennessee; Texas; Utah; Vermont; Virginia; Washington; West Virginia; Wisconsin; Wyoming.</td>
<td><table>
<colgroup>
<col style="width: 0%" />
<col style="width: 99%" />
</colgroup>
<thead>
<tr>
<th></th>
<th>Replaces NGVD29 height (ftUS) (CRS code 5702).</th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td>US survey foot</td>
<td>Up</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
