import csv
import xml.etree.ElementTree as ET


def importData(filePath, dataList, fieldNamesList, csvFile, results=[]):
    for dataType in dataList:
        results.append(dataHelper(filePath, dataType))
    with open(csvFile, 'r') as csv_file:
        csvReader = csv.DictReader(csv_file)

        with open(f"new_{csvFile}", 'w') as newFile:
            fieldnames = fieldNamesList
            csvWriter = csv.DictWriter(
                newFile, fieldnames=fieldnames, extrasaction='ignore')
            csvWriter.writeheader()
            for line in csvReader:
                csvWriter.writerow(line)
    return results


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
