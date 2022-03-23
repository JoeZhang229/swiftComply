from dataTransfer import importData
# Run this file to run the script, which will import data
# from the Facility.xml file into a new properties csv.

# importData is the main function, its main parameters are:
# (filePath, dataList, fieldNamesList, csvFile)

# pick the headers you want to export from the XML in the dataList variable,
# and corresponding fieldnames in the fieldNamesList variable

dataList = ['Facility_ID', 'Facility_Account_Number',
            'Facility_Name', 'Service_Address_Street_Name', 'Service_Address_City', 'Service_Address_State', 'Service_Address_Zip_Code', 'Facility_Contact_Mgr_ID']
fieldNamesList = ['property_id', 'account_number', 'name', 'address1',
                  'city', 'state_prov', 'postal_code', 'primary_contact_id']

importData('./XC2 Export Data/Facility.xml',
           dataList, fieldNamesList, 'properties.csv')
