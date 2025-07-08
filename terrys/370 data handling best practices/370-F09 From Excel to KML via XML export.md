---
title: "370-F09 From Excel to KML via XML export"
source_file: "C:\Users\tchernen\handbook_docx\4_Data_Repository\terrys\370 data handling best practices\370-F09 From Excel to KML via XML export.docx"
review_period: "3 years"
created_by: "Terry Curran"
---

**340-F09**

**From Excel to KML via XML export**

August 6, 2015

There are a number of different ways to get data from Microsoft Excel into Google Earth. There are various web-based tools to do the job, such as the one we mentioned in [<u>this post</u>](http://www.gearthblog.com/blog/archives/2008/02/links_spacenavigator_contest_excel.html). Another way is to do the conversion entirely in Excel as demonstrated by GEB reader “Will from the UK” in [<u>this post</u>](http://www.gearthblog.com/blog/archives/2011/02/tools_to_help_the_armchair_archeolo.html).

Today we are looking at the technique we used for [<u>this post</u>](http://www.gearthblog.com/blog/archives/2015/07/satellite-imagery-updates-layer-another-look.html) where we wanted to export a set of polygons that we had previously imported into Excel from a KML. Importing from KML is as easy as renaming the file from .kml to .xml and then using Excel’s built in import features.

We used Excel 2013, but the process should be similar in most recent versions of Excel. The first step is to enable the ‘Developer’ tab as described [<u>here</u>](http://www.excel-easy.com/examples/developer-tab.html). Next, make sure your data is arranged in the columns ‘name’, ‘description’, ‘styleUrl’ and ‘coordinates’. Open the ‘XML Source’ task pane by clicking on the ‘Source’ button found on the ‘Developer’ toolbar. Next, click the ‘XML Maps’ button. If you had previously imported data from KML, you may already have an XML Map listed. If so, delete it. Now download [<u>this file</u>](http://www.gearthblog.com/kmfiles/KML_Map.xml) and add it as an XML Map. Excel will use it to create a schema. Close any dialog boxes and you should now have something like this:

<img src="370-F09 From Excel to KML via XML export_media/media/image1.jpeg" style="width:6.25044in;height:4.46742in" alt="http://www.gearthblog.com/wp-content/uploads/2015/08/ExcelToKML1.jpg" />

Drag and drop the column names from the ‘XML Source’ pane to the appropriate column headers. It should now look something like this:

<img src="370-F09 From Excel to KML via XML export_media/media/image2.jpeg" style="width:7.04028in;height:5.03194in" alt="http://www.gearthblog.com/wp-content/uploads/2015/08/ExcelToKML2.jpg" />

Click the ‘Export’ button found on the ‘Developer’ toolbar. Choose a file name and export the data. Edit the resulting file using any text editor. Replace all the text above the first \<Placemark\> tag with this:

\<?xml version="1.0" encoding="UTF-8"?\>  
\<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom"\>  
\<Folder\>

Then scroll to the bottom and replace the \</data-set\> tag with this:

\</Folder\>  
\</kml\>

Save the file and rename it from .xml to .kml. You should now be able to open it in Google Earth. Finally, you may wish to add in some style information to your KML, which you can either do by editing the KML file, or from within Google Earth.

The above procedure was specifically designed for polygons. For other types of KML objects, modify the XML Map file to match the types of objects you wish to export.

Although Excel readily imports KMLs with Placemarks arranged into folders, we were not able to get it to export folders. All attempts to do so resulted in an error stating that the XML map contained ‘denormalized data’.

We worked out how to do the above export with help from [<u>here</u>](http://www.excel-easy.com/examples/xml.html).

<img src="370-F09 From Excel to KML via XML export_media/media/image3.jpeg" style="width:0.62083in;height:0.62083in" alt="http://0.gravatar.com/avatar/92e68eff17388e59c80388fbe5d70b7d?s=90&amp;d=mm&amp;r=g" />

**About Timothy Whitehead**

Timothy has been using Google Earth since 2004 when it was still called Keyhole before it was renamed Google Earth in 2005 and has been a huge fan ever since. He is a programmer working for [<u>Red Wing Aerobatx</u>](http://www.redwingaerobatx.com) and lives in Cape Town, South Africa.

- [<u>Google+</u>](https://plus.google.com/u/0/+TimothyWhiteheadzm/posts?rel=author)

> \|

- [<u>More Posts (415)</u>](http://www.gearthblog.com/blog/archives/author/timothy)
