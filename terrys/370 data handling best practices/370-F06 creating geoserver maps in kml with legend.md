**340-F06**

**Typical GeoNetwork « online distribution » script**

\<gmd:onLine\>

\<gmd:CI_OnlineResource\>

\<gmd:linkage\>

\<gmd:URL\>http://soggy.zoology.ubc.ca:8080/geoserver/wms/\</gmd:URL\>

\</gmd:linkage\>

\<gmd:protocol\>

\<gco:CharacterString\>OGC:WMS-1.3.0-http-get-map\</gco:CharacterString\>

\</gmd:protocol\>

\<gmd:name\>

\<gco:CharacterString\>psf:bc_shorezone\</gco:CharacterString\>

\</gmd:name\>

\<gmd:description\>

\<gco:CharacterString\>bc shorezone shapefile\</gco:CharacterString\>

\</gmd:description\>

\</gmd:CI_OnlineResource\>

\</gmd:onLine\>

***NOTES:***

1.  Name – 1<sup>st</sup> line in regular display and label for local map (if WMS); 2<sup>nd</sup> otherwise

2.  Description – 2<sup>nd</sup> line in regular display (if WMS); 1<sup>st</sup> otherwise

3.  Feel free to edit the protocol. For instance, append kml to wms if want Globe Viewer link.

**  **

**KML Reflector[<u>¶</u>](http://docs.geoserver.org/stable/en/user/services/wms/googleearth/features/kmlreflector.html#kml-reflector)**

Standard WMS requests can be quite long and cumbersome. The following is an example of a request for KML output from GeoServer:

http://localhost:8080/geoserver/ows?service=WMS \\

&request=GetMap&version=1.1.1 \\

&format=application/vnd.google-earth.kml+XML \\

&width=1024&height=1024 \\

&srs=EPSG:4326 \\

&layers=topp:states \\

&styles=population \\

&bbox=-180,-90,180,90

GeoServer includes an alternate way of requesting KML, and that is to use the **KML reflector**. The KML reflector is a simpler URL-encoded request that uses sensible defaults for many of the parameters in a standard WMS request. Using the KML reflector one can shorten the above request to:

http://localhost:8080/geoserver/wms/kml?layers=topp:states

**Using the KML reflector**

The only mandatory parameter is the layers parameter. The syntax is as follows:

http://GEOSERVER_URL/wms/kml?layers=\<layer\>

where GEOSERVER_URL is the URL of your GeoServer instance, and \<layer\> is the name of the featuretype to be served.

The following table lists the default assumptions:

| **Key**     | **Value**                             |
|-------------|---------------------------------------|
| request     | GetMap                                |
| service     | wms                                   |
| version     | 1.1.1                                 |
| srs         | EPSG:4326                             |
| format      | applcation/vnd.google-earth.kmz+xml   |
| width       | 2048                                  |
| height      | 2048                                  |
| bbox        | \<layer bounds\>                      |
| kmattr      | true                                  |
| kmplacemark | false                                 |
| kmscore     | 40                                    |
| styles      | \[default style for the featuretype\] |

<http://soggy.zoology.ubc.ca:8080/geoserver/wms/kml?REQUEST=GetLegendGraphic&VERSION=1.0.0&FORMAT=image/png&WIDTH=20&HEIGHT=50&stle=psf:ShoreZone_RepType>

To get GeoServer to include a legend with the KML output, append legend=true to the KML reflector request. For example:

http://soggy.zoology.ubc.ca:8080/geoserver/wms/kml?REQUEST=GetLegendGraphic&VERSION=1.0.0&FORMAT=image/png&WIDTH=20&HEIGHT=50&stle=psf:ShoreZone_RepType&legend=true
