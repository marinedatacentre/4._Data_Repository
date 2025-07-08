---
process_number: 346-10
title: Erddap  installation
author: Terry Curran
created: 2021-04-16
modified: 2021-12-25
review_period: 3 years
---

**Purpose:**

To install ERDDAP (the NOAA Environmental Research Division's Data Access Program) on a suitable server as a service (daemon). ERDDAP is a data server that gives you a simple, consistent way to download subsets of gridded and tabular scientific datasets in common file formats and make graphs and maps.

**ERDDAP unifies the different types of data servers so you have a consistent way to get the data you want, in the format you want.**

- ERDDAP acts as a middleman between you and various remote data servers. When you request data from ERDDAP, ERDDAP reformats the request into the format required by the remote server, sends the request to the remote server, gets the data, reformats the data into the format that you requested, and sends the data to you. You no longer have to go to different data servers to get data from different datasets.

- ERDDAP offers an easy-to-use, consistent way to request data: via the OPeNDAP standard. Many datasets can also be accessed via ERDDAP's Web Map Service (WMS).

- ERDDAP returns data in the common file format of your choice. ERDDAP offers all data as .html table, ESRI .asc and .csv, Google Earth .kml, OPeNDAP binary, .mat, .nc, ODV .txt, .csv, .tsv, .json, and .xhtml. So you no longer have to waste time and effort reformatting data.

- ERDDAP can also return a .png or .pdf image with a customized graph or map.

- ERDDAP standardizes the dates+times in the results. Data from other data servers is hard to compare because the dates+times often are expressed in different formats (for example, "Jan 2, 2018", 02-JAN-2018, 1/2/18, 2/1/18, 2018-01-02, "days since Jan 1, 1900"). For string times, ERDDAP always uses the ISO 8601:2004(E) standard format, for example, 2018-01-02T00:00:00Z. For numeric times, ERDDAP always uses "seconds since 1970-01-01T00:00:00Z". ERDDAP always uses the Zulu (UTC, GMT) time zone to remove the difficulties of working with different time zones and standard time versus daylight saving time. ERDDAP has [a service to convert a string time to/from a numeric time](https://coastwatch.pfeg.noaa.gov/erddap/convert/time.html).

- ERDDAP has web pages (for humans with browsers) and [RESTful web services](https://coastwatch.pfeg.noaa.gov/erddap/rest.html) (for computer programs). You can bypass ERDDAP's web pages and use ERDDAP's RESTful web services (for example, for searching for datasets, for downloading data, for making maps) directly from any computer program (for example, Matlab, R, or a program that you write) and even from web pages (via HTML image tags or JavaScript). You can also build other useful and interesting things on top of ERDDAP's web services — see the [Awesome ERDDAP<img src="346-10 Erddap  installation_media/media/image1.png" style="width:0.1875in;height:0.125in" />](https://github.com/IrishMarineInstitute/awesome-erddap) list of awesome ERDDAP-related projects.

Linux versions all strongly prefer that applications be installed via a Package Manager, and this process uses the RPM package installed by DNF on RHEL8. ERDDAP requires Java 8 exclusively.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 51%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Step</strong></th>
<th><strong>Major Activity</strong></th>
<th><strong>References, Forms and Details</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">1</td>
<td><p>Switch to superuser</p>
<blockquote>
<p>sudo -i</p>
</blockquote></td>
<td><ul>
<li><p>Need frequent higher privileges, and this saves re-entering pw.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td>Set up Java 8, if not already done. Refer to process 310-06, or 310-08 for multiple Java versions.</td>
<td><ul>
<li><p>ERDDAP requires Java 8 only.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td>Install a webserver such as Tomcat or Jetty. Refer to 330-20 (Jetty) or 334-10 (Tomcat).</td>
<td><ul>
<li><p>Should see a splash screen when operational</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td><p>Download erddap cofiguration files:</p>
<ul>
<li><p>wget <a href="https://github.com/BobSimons/erddap/releases/download/v2.14/erddapContent.zip">https://github.com/BobSimons/erddap/releases/download/v2.14/erddapContent.zip</a></p></li>
</ul>
<ul>
<li><p>unzip it into a suitable location, creating content/erddap</p></li>
<li><p>content should be owned by the webserver id, and owner rwx only</p></li>
</ul></td>
<td><ul>
<li><p>version 2.14, 19,826 bytes</p></li>
<li><p>MD5=8C9FCE5C47654BCC7F7E924A935755E7</p></li>
<li><p>dated 2021-07-02</p></li>
</ul>
<ul>
<li><p>‘content’ variable must be specified</p>
<ul>
<li><p>in the webserver.service exec statement if using daemons, or</p></li>
<li><p>in a /<em>etc/</em>profile.d shell (see below)</p></li>
</ul></li>
<li><p>contents of {location} should be datasets.xml, images/ and setup.xml</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td><p>Define environmental variables, either permanently in file /etc/profile.d/{vars}.sh :</p>
<ul>
<li><p>JAVA_HOME</p></li>
<li><p>other variables as desired</p></li>
</ul>
<p>Alternatively, if planning to use daemons for webserver auto-start, they can be defined in the Daemon ‘Exec’ statement.</p></td>
<td><ul>
<li><p>replace {vars} with installer-chosen name</p></li>
<li><p><u>Sample content:</u></p></li>
</ul>
<p># Set JDK installation directory according to selected Java compiler</p>
<p>export JAVA_HOME=$(readlink -f /usr/bin/javac | sed "<a href="../../../../../../../s:/bin/javac">s:/bin/javac</a>::")</p>
<p># Set other variables (e.g.webserver) as desired:</p>
<p>export JETTY_HOME=/usr/share/java/jetty-distribution-9.4.44.v20210927/</p>
<p>export JETTY_BASE=/var/www/jettybase</p></td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td><p>Check that DejaVu fonts are present</p>
<p>fc-list | grep -i "DejaVu"</p></td>
<td><ul>
<li><p>Already included in many OS distributions</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: left;"><p>If not, then it is recommended to download the fonts:</p>
<p>https://coastwatch.pfeg.noaa.gov/erddap/download/DejaVuFonts.zip</p>
<p>And unzip to</p>
<p>JAVA_HOME/lib/fonts</p></td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td><p>Edit the setup.xml file in the ‘content’ directory:</p>
<ul>
<li><p>vi setup.xml</p></li>
<li><p>For the initial setup, you MUST at least change these settings:</p></li>
<li><p>&lt;bigParentDirectory&gt;</p></li>
<li><p>&lt;baseUrl&gt;</p></li>
<li><p>&lt;emailEverythingTo&gt;</p></li>
<li><p>&lt;email*&gt;</p></li>
<li><p>&lt;admin*&gt;</p></li>
<li><p>flagKeyKey</p></li>
<li><p>&lt;baseHttpsUrl&gt; (if you set up https:)</p></li>
<li><p>If using other than DejaVu Sans fonts, then also update</p></li>
<li><p>fontFamily</p></li>
</ul></td>
<td><ul>
<li><p>You <em><strong>must change</strong></em> the provided defaults or the application will not load. The only exception to this is the font selection.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">9</td>
<td><p><u>Tomcat webserver only:</u></p>
<p><a href="https://coastwatch.pfeg.noaa.gov/erddap/download/setup.html#server.xml">server.xml</a> - In <em>tomcat</em>/conf/server.xml file, there are two changes that you should make to each of the two &lt;Connector&gt; tags (one for '&lt;Connector port="8080" ' and one for '&lt;Connector port="8443" '):</p>
<ul>
<li><p>(Recommended) Increase the parameter</p></li>
<li><p>connectionTimeout</p></li>
<li><p>(Recommended) Add a new parameter: relaxedQueryChars="[]|"</p></li>
</ul></td>
<td><ul>
<li><p>Not needed if using jetty webserver</p></li>
<li><p>connectionTimeout value perhaps to 300000 (milliseconds), which is 5 minutes.</p></li>
<li><p>The ‘relaxedQueryChars’ parameter is optional and slightly less secure, but removes the need for users to percent-encode these characters when they occur in the parameters of a user's request URL.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">10</td>
<td><p><u>Tomcat webserver only:</u></p>
<p>In the[tomcat]/conf/context.xml file, increase the maximum size of the cache. Add this tag immediately before &lt;/Context&gt; :</p>
<p>&lt;Resources cachingAllowed="true" cacheMaxSize="80000" /&gt;<br />
(or some other number, in KB.)</p></td>
<td><ul>
<li><p>To avoid Tomcat throwing warnings during startup about</p></li>
</ul>
<blockquote>
<p>"org.apache.catalina.webresources.Cache.getResource Unable to add the resource at <em>someFile”</em></p>
</blockquote>
<ul>
<li><p>to the cache because there was insufficient free space available after evicting expired cache entries</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">11</td>
<td style="text-align: left;"><blockquote>
<p><u>If using an Apache proxy:</u></p>
<p>Modify the Apache httpd.conf file (usually in /etc/httpd/conf/ ):</p>
</blockquote>
<ul>
<li><p>Change the existing &lt;Timeout&gt; setting (or add one at the end of the file) to 3600 (seconds), instead of the default 60 or 120 seconds.</p></li>
<li><p>Change the existing &lt;ProxyTimeout&gt; setting (or add one at the end of the file) to 3600 (seconds), instead of the default 60 or 120 seconds.</p></li>
</ul>
<ul>
<li><p>Restart Apache:</p></li>
</ul>
<blockquote>
<p>/usr/sbin/apachectl -k graceful</p>
<p>(but sometimes it is in a different directory).</p>
</blockquote></td>
<td style="text-align: left;"><blockquote>
<p>If exists, change the Apache proxy timeout settings.</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;">12</td>
<td><p>Install webserver as a daemon</p>
<ul>
<li><p>Process 334-10 Set up tomcat, or</p></li>
<li><p>Process 330-20 Set up Jetty</p></li>
</ul></td>
<td><ul>
<li></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">13</td>
<td>Extract the erddap.war into the /webapp/ folder</td>
<td><ul>
<li><p>Do not allow jetty to deploy the war or you will then need to specify the erddalContentsDirectory location</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">14</td>
<td><p>Create the webserver daemon in</p>
<p>/etc<em>/</em>systemd/system/</p></td>
<td style="text-align: left;"><p>Samples are:</p>
<ul>
<li><p>346-F10 jetty.service</p></li>
<li><p>346-F20 tomcat.service</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">15</td>
<td><p>Reload the daemons</p>
<p>systemctl daemon-reload</p></td>
<td><ul>
<li><p>Need to be superuser (sudo prefix)</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">16</td>
<td><p>Enable the daemon to start automatically</p>
<p>systemctl enable {webserver}.service</p></td>
<td><ul>
<li><p>Need to be superuser (sudo prefix)</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">17</td>
<td><p>After a minute to allow initialization, check status</p>
<p>systemctl status {webserver}.service</p></td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">18</td>
<td><p>Check for erddap operation</p>
<p><a href="http://ip/">http://{ip</a> address}/erddap</p></td>
<td><ul>
<li><p>{ip address} can be ‘localhost’ if testing locally</p></li>
<li><p>should see erdap splash screen</p></li>
</ul></td>
</tr>
</tbody>
</table>
