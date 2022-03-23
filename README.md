# Instructions

In Python Version 3.9.4+, run the dataVariables.py file to run the script, which will import data from the ```Facility.xml``` file into a new properties csv based on the ```properties.csv``` file format.

**all arguments are accepted as strings**

```importData``` is the main function, its main arguments are:

```(importFilePath, importDataList, fieldNamesList, csvFilePath)```


Choose the XML elements you want to export from the XML in the importDataList variable as a string in the list structure, and corresponding fieldnames in the fieldNamesList variable in the same format.

**IMPORTANT - order matters for both importDataList and fieldNamesList as they correspond to each other**

## Examples

I want to import Facility ID and Facility Account Number in the XML file.

In the XML file the Facility Account Number is labelled as "Facility_Account_Number" as an Element.

```importDataList = ['Facility_ID', 'Facility_Account_Number']```

```fieldNamesList = ['property_id', 'account_number']```

```'Facility_ID'```and ```'property_id'``` are both in their respective positions because they correspond with each other, same with ```'Facility_Account_Number'``` and ```'account_number'```.
