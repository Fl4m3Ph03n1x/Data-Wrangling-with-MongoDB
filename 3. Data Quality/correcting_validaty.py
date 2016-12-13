"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in the range as described above,
  write that line to the output_good file
- if the value of the field is not a valid year as described above, 
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the 
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import pprint

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

URI_DBPEDIA = 'dbpedia.org'
MIN_YEAR = 1886
MAX_YEAR = 2014

def isInt(string):
    try: 
        int(string)
        return True
    except ValueError:
        return False

def process_file(input_file, output_good, output_bad):


    dbpediadata = {"good": [], "bad": [] }
    with open(input_file, "r") as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames
        for row in reader:
            if (row["URI"].find(URI_DBPEDIA) > -1):
                row["productionStartYear"] = row["productionStartYear"][:4]
                if isInt(row["productionStartYear"]) and int(row["productionStartYear"]) > MIN_YEAR and int(row["productionStartYear"]) < MAX_YEAR:
                    dbpediadata["good"].append(row)
                else:
                    dbpediadata["bad"].append(row)
    
    # This is just an example on how you can use csv.DictWriter
    # Remember that you have to output 2 files
    with open(output_good, "w") as goodFile:
        writer = csv.DictWriter(goodFile, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in dbpediadata["good"]:
            writer.writerow(row)
    
    with open(output_bad, "w") as badFile:
        writer = csv.DictWriter(badFile, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in dbpediadata["bad"]:
            writer.writerow(row)


def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()