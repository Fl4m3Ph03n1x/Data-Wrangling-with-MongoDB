#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import sys
import xlrd
from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data.xls"

# check for int info http://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints
def findMax(list):
    index = 0
    maxIndex = -1
    maxVal = -sys.maxint - 1
    for entry in list:
        if entry > maxVal:
            maxVal = entry
            maxIndex = index
        index += 1
    
    return {"maxVal": maxVal, "maxIndex": maxIndex}

def findMin(list):
    index = 0
    minIndex = -1
    minVal = sys.maxint
    for entry in list:
        if entry < minVal:
            minVal = entry
            minIndex = index
        index += 1
    
    return {"minVal": minVal, "minIndex": minIndex}

def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    
    datesDict = sheet.col(0, start_rowx=1, end_rowx=None)
    coastDict = sheet.col(1, start_rowx=1, end_rowx=None)
    coastList = []
    
    for entry in coastDict:
        coastList.append(entry.value)
    
    maxInfo = findMax(coastList)
    minInfo = findMin(coastList)
    
    data = {
            'maxtime': xlrd.xldate_as_tuple(datesDict[maxInfo["maxIndex"]].value, 0),
            'maxvalue': maxInfo["maxVal"],
            'mintime': xlrd.xldate_as_tuple(datesDict[minInfo["minIndex"]].value, 0),
            'minvalue': minInfo["minVal"],
            'avgcoast': sum(coastList) / len(coastList)
    }
    return data


def test():
    # open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)

test()
        