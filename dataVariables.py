from dataTransfer import importData
# Run this file to run the script

# XML file elements you want to import from
importDataList = ['Facility_ID', 'Facility_Account_Number',
                  'Facility_Name', 'Service_Address_Street_Name', 'Service_Address_City', 'Service_Address_State', 'Service_Address_Zip_Code', 'Facility_Contact_Mgr_ID']

# CSV headers you want to export
fieldNamesList = ['property_id', 'account_number', 'name', 'address1',
                  'city', 'state_prov', 'postal_code', 'primary_contact_id']

importData('./XC2 Export Data/Facility.xml',
           importDataList, fieldNamesList, './SC Backflow CSV Import Examples/properties.csv')
