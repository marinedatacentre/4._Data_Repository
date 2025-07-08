---
title: "370-07 Creating and Styling a GeoServer Layer"
source_file: "C:\Users\tchernen\handbook_docx\4_Data_Repository\terrys\370 data handling best practices\370-07 Creating and Styling a GeoServer Layer.docx"
review_period: "3 years"
created_by: "Peter"
created: "2015-02-24"
modified: "2019-09-10"
---

**Purpose:**

This document describes how to add a simple spatial layer in GeoServer. The intention is to quickly expose a data layer for use by GeoNetwork. This will be linked from a metadata record stored in GeoNetwork.

This is well described in the GeoServer User manual, along with extensive and advanced styling considerations not discussed here.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 50%" />
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
<td style="text-align: left;">Sign onto GeoServer, providing an ID and password with administrator privileges</td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: left;">Create a workspace</td>
<td>This is a way of grouping layers, for instance from a single supplier or by theme</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: left;">Identify a store</td>
<td>This is a location where similar data is stored. Common instances include a folder of shp files, and one or more tables containing spatial data within a database.</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: left;"><p>Create a Style (optional)</p>
<ul>
<li><p>Click on “style”</p></li>
<li><p>Enter a short title</p></li>
<li><p>Select “copy from”</p></li>
<li><p>Make changes</p></li>
<li><p>Select “validate” at bottom, scroll to top to see if okay</p></li>
<li><p>Select “submit”</p></li>
</ul></td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: left;"><p>Create a layer</p>
<ul>
<li><p>Click “add a new resource”</p></li>
<li><p>Choose &lt;workspace&gt;: &lt;atlasLayer&gt;</p>
<ul>
<li><p>Click “publish” to open the layer for editing</p></li>
</ul></li>
</ul></td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: left;"><p>Editing – First tab (Data)</p>
<ul>
<li><p>Name – don’t change, because it will link to the layer</p></li>
<li><p>Title – change to something reasonable, but short. Spaces encouraged.</p></li>
<li><p>Coordinate reference system. Choose something appropriate (e.g. EPSG:3005)</p></li>
<li><p>Bounding Boxes</p>
<ul>
<li><p>Click “compute from data”</p>
<ul>
<li><p>Should generally be in range 0 to 1,000,000</p></li>
</ul></li>
<li><p>Click “compute from native bounds”</p>
<ul>
<li><p>Geographic: longMin, latMin, longMax, latMax</p></li>
</ul></li>
</ul></li>
</ul></td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: left;"><p>Editing – Second tab (Publishing)</p>
<ul>
<li><p>Style</p>
<ul>
<li><p>choose one, or accept Default</p></li>
</ul></li>
<li><p>Save (at bottom of page)</p></li>
</ul></td>
<td><ul>
<li><p>Saves the layer</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td style="text-align: left;"><p>Layer Preview</p>
<ul>
<li><p>On layer of choice, select</p>
<ul>
<li><p>Open Layers</p>
<ul>
<li><p>May need to pan and zoom to see result</p></li>
</ul></li>
<li><p>Google Earth</p>
<ul>
<li><p>Should display properly (without big red X)</p></li>
</ul></li>
</ul></li>
</ul></td>
<td><ul>
<li><p>If Google result displays red X, determine what is wrong and fix</p></li>
<li><p>Otherwise, layer is available for linking to metadata</p></li>
</ul></td>
</tr>
</tbody>
</table>
