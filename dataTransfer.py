import csv
import xml.etree.ElementTree as ET


def importData(file1, *args, **kwargs):
    # with open(file1, 'r') as file1:
    #     file1_read = csv.reader(file1)

    #     for line in file1_read:
    # elementTree obj
    tree = ET.parse(file1)
    root = tree.getroot()
    for facility in root.findall('T_Facility'):
        # print(ET.tostring(facility))
        facilityId = facility.find('Facility_ID').text
        print(facilityId)

# root=tree2.getroot()
# for element in root.findall('Facility_ID'):
#     id = element.text
#     print(id)
# for facility in root.findall('T_Facility'):
# print(ET.tostring(facility))
# facilityId=facility.find('Facility_ID').text
# print(facility)


print(importData('./XC2 Export Data/Facility.xml'))
