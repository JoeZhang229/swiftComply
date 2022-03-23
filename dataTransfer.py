import csv
import xml.etree.ElementTree as ET


def importData(importFilePath, dataList, fieldNamesList, csvFilePath, results=[]):
    # import data from XML based on dataList entries
    for dataType in dataList:
        results.append(dataHelper(importFilePath, dataType))
    with open(csvFilePath, 'r') as csv_file:
        csvReader = csv.DictReader(csv_file)
        # write csv based on headers in fieldnames
        with open("new_properties.csv", 'w') as newFile:
            fieldnames = fieldNamesList
            # extrasaction ignores headers not included in fieldnames
            csvWriter = csv.DictWriter(
                newFile, fieldnames=fieldnames, extrasaction='ignore')
            csvWriter.writeheader()
            for line in csvReader:
                csvWriter.writerow(line)
    return results


# helper function based on XML header
def dataHelper(file, dataType, results=[]):
    # elementTree obj
    tree = ET.parse(file)
    root = tree.getroot()
    facilities = root.findall('T_Facility')
    for facility in facilities:
        # grabs facility data based on type
        facilityData = facility.find(dataType)
        # fixes strange error with None object appearing while parsing through XML
        if facilityData is None:
            continue
        else:
            results.append(facilityData.text)
    return results
