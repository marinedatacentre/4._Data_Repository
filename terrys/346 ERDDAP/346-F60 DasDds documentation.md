[**DasDds**](https://coastwatch.pfeg.noaa.gov/erddap/download/setupDatasetsXml.html#DasDds) is a command line program that you can use after you have created a first attempt at the XML for a new dataset in datasets.xml. With DasDds, you can repeatedly test and refine the XML. When you use the DasDds program:

- On Windows, the first time you run DasDds, you need to edit the DasDds.bat file with a text editor to change the path to the java.exe file so that Windows can find Java.

- DasDds asks you for the datasetID for the dataset you are working on.

- DasDds tries to create the dataset with that datasetID.

  - DasDds always prints lots of diagnostic messages.  
    If you use "DasDds -verbose", DasDds will print more diagnostic messages than usual.

  - For safety, DasDds always deletes all of the cached dataset information (files) for the dataset before trying to create the dataset. This is the equivalent of setting a [hard flag](https://coastwatch.pfeg.noaa.gov/erddap/download/setup.html#hardFlag) So for aggregated datasets, you might want to adjust the fileNameRegex temporarily to limit the number of files the data constructor finds.

  - If the dataset fails to load (for whatever reason), DasDds will stop and show you the error message for the first error it finds.  
    **Don't try to guess what the problem might be. Read the ERROR message carefully.**  
    If necessary, read the preceding diagnostic messages to find more clues and information, too.

  - **Make a change to the dataset's XML to try to solve THAT problem**  
    and let DasDds try to create the dataset again.

  - **If you repeatedly solve each problem, you will eventually solve all the problems**  
    and the dataset will load.

- All DasDds output (diagnostics and results) are written to the screen and to *bigParentDirectory*/logs/DasDds.log .

- If DasDds can create the dataset, DasDds will then show you the [.das (Dataset Attribute Structure)](https://coastwatch.pfeg.noaa.gov/erddap/griddap/documentation.html#fileType_das), [.dds (Dataset Descriptor Structure)](https://coastwatch.pfeg.noaa.gov/erddap/griddap/documentation.html#fileType_dds), and [.timeGaps (time gaps)](https://coastwatch.pfeg.noaa.gov/erddap/griddap/documentation.html#timeGaps) information for the dataset on your screen and write them to *bigParentDirectory*/logs/DasDds.out .

- Often, you will want to make some small change to the dataset's XML to clean up the dataset's metadata and rerun DasDds.
