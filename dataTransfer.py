import csv
import xml.etree.ElementTree as ET


def importData(filePath, dataList, results=[]):
    for dataType in dataList:
        results.append(dataHelper(filePath, dataType))
    return results


def dataHelper(file, dataType):
    results = []
    # with open(file, 'r') as file:
    #     file1_read = csv.reader(file)

    #     for line in file1_read:
    # elementTree obj
    tree = ET.parse(file)
    root = tree.getroot()
    facilities = root.findall('T_Facility')
    for facility in facilities:
        # grabs facility data based on type
        facilityData = facility.find(dataType)
        if facilityData is None:
            continue
        else:
            # print(facilityData.text)
            results.append(facilityData.text)
    return results


dict = ['Facility_ID', 'Facility_Account_Number', 'Facility_Name']

# print(dataHelper('./XC2 Export Data/Facility.xml', 'Facility_ID'))
# print(dataHelper('./XC2 Export Data/Facility.xml', 'Facility_Account_Number'))
# print('Names', dataHelper('./XC2 Export Data/Facility.xml', 'Facility_Name'))
# print(importData('./XC2 Export Data/Facility.xml', dict))
print(importData('./XC2 Export Data/Facility.xml', dict))
