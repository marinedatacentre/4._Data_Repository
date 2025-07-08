---
process_number: 640-01
title: DarwinCoreIntro_250128
author: Paulina Salinas Ruiz
created: 2025-01-16
modified: 2025-01-29
review_period: 3 years
---

**Purpose:**

The purpose of this process is to provide a systematic approach for converting any dataset into the Darwin Core (DwC) format, ensuring data are standardized, interoperable, and ready for sharing and integration within biodiversity and ecological research frameworks.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 42%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Step</strong></th>
<th style="text-align: center;"><strong>Major Activity</strong></th>
<th style="text-align: center;"><strong>References, Forms and Details</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">1 </td>
<td><blockquote>
<p>Familiarize yourself with Darwin Core terms and their definitions, and review the core classes (Occurrence, Taxon, Event, and Location). Determine which class(es) best fit your dataset.</p>
</blockquote></td>
<td><blockquote>
<p>Refer to the <a href="https://manual.obis.org/darwin_core.html">Core Terms and Guidelines</a> to obtain more context on the different classes.</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;">2 </td>
<td><blockquote>
<p>Assess and prepare your dataset</p>
</blockquote></td>
<td><ul>
<li><p><strong>Examine your dataset:</strong> identify the fields and data types available</p></li>
<li><p><strong>Match the fields to DwC terms:</strong> create a mapping between your dataset fields (usually column headers) and <a href="https://dwc.tdwg.org/terms/">Darwin Core terms.</a> i.e. “Species Name” 🡪 scientificName</p></li>
<li><p><strong>Address data gaps:</strong> note any missing DwC-required fields and plan on how to populate them.</p></li>
<li><p><strong>Standardize field values:</strong> ensure data aligns with DwC standards (i.e. use ISO 8601 for dates)</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">3 </td>
<td><blockquote>
<p>Clean and transform the data</p>
</blockquote></td>
<td><ul>
<li><p><strong>Remove duplicates</strong>: make sure each record is unique</p></li>
<li><p><strong>Correct errors:</strong> fix typos, outliers, or inconsistent formats (i.e. convert coordinates to decimal degrees).</p></li>
<li><p><strong>Standardize taxonomic names:</strong> validate species names using authoritative sources like <a href="https://www.gbif.org/dataset/d7dddbf4-2cf0-4f39-9b2a-bb099caae36c">GBIF</a> or <a href="https://www.usgs.gov/tools/integrated-taxonomic-information-system-itis">ITIS</a>.</p></li>
<li><p><strong>Add missing fields:</strong> populate missing information where possible.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td><blockquote>
<p>Map fields to Darwin Core terms</p>
</blockquote></td>
<td><ul>
<li><p>Create a new spreadsheet or database table with columns labeled using Darwin Core terms.</p></li>
<li><p>Populate columns using your mapped dataset fields.</p></li>
<li><p>Include any additional DwC fields relevant to your dataset. i.e. basisOfRecord, recordedBy.</p></li>
<li><p>Note: refer to this example:</p>
<ul>
<li><p><a href="https://pacificsalmonfoundation-my.sharepoint.com/:x:/g/personal/psalinasruiz_psf_ca/EXNPizYiqhdDlbmW5RmIjoYBbxdxNZ7GUJy2wyLVyMgyiA?e=W7rsbG">Original dataset</a></p></li>
<li><p>Reformatted data:</p>
<ul>
<li><p><a href="https://pacificsalmonfoundation-my.sharepoint.com/:x:/g/personal/psalinasruiz_psf_ca/EYslTkkF9D9EnegYCLos-ksBaw0TRwnNeNpldPEmJtPf-w?e=VrwX7w">Event Core</a></p></li>
<li><p><a href="https://pacificsalmonfoundation-my.sharepoint.com/:x:/g/personal/psalinasruiz_psf_ca/ETpdRaCX991HgtsWqwV8B0AB5mBc4LeEu2_t3asO4LoCgQ?e=W20liw">Occurrence Core</a></p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td><blockquote>
<p>Validate the Dataset</p>
</blockquote></td>
<td><ul>
<li><p>Use tools like the <a href="https://www.gbif.org/tool/81281/gbif-data-validator">GBIF Darwin Core Archive Validator</a> to check for compliance.</p></li>
<li><p>Address validation errors, such as missing mandatory fields or invalid formats.</p></li>
<li><p><strong>Note</strong>: if the dataset is planned to be uploaded to OBIS, their metadata platform automatically validates it, so no need for an external validator.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td><blockquote>
<p>Generate a Darwin Core Archive (DwC-A)</p>
</blockquote></td>
<td><ul>
<li><p>Organize your data into the required DwC-A structure:</p>
<ul>
<li><p>A core file (i.e. event or occurrence core)</p></li>
<li><p>A meta.xml file (metadata)</p></li>
<li><p>Optional extensions (i.e. measurementOrFact)</p></li>
</ul></li>
<li><p>Use tools like the <a href="https://www.gbif.org/ipt">GBIF Integrated Publishing Toolkit (IPT)</a> to package the dataset.</p></li>
<li><p><strong>Note</strong>: this step is NOT needed if the dataset is planned to be uploaded to OBIS.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td><blockquote>
<p>Publish or share the dataset</p>
</blockquote></td>
<td><ul>
<li><p>Share the dataset via an IPT and/or upload to platforms like <a href="https://www.gbif.org/ipt">GBIF</a>, <a href="https://cioos-siooc.github.io/metadata-entry-form/#/en/pacific/new">CIOOS</a>, <a href="https://ipt.iobis.org/obiscanada/">OBIS</a>, and our <a href="https://soggy2.zoology.ubc.ca/geonetwork/srv/eng/catalog.search#/home">Data Portal</a>.</p></li>
<li><p>Make sure to include metadata.</p></li>
</ul></td>
</tr>
</tbody>
</table>
