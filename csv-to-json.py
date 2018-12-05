import csv
import json

csvfile = open('data-clean.csv', 'r')
jsonfile = open('data.json', 'w')

fieldnames = ("yyyy-mm","day","time","unixtime","inTempC","inTempF","outTempC","outTempF","pressure","inRH","outDewptF","avgWind","gustWind")
reader = csv.DictReader( csvfile, fieldnames)
next(reader, None) #skip first line with headers

row_number = 2 #keep track of where we are in the data.csv file

# leading bracket
jsonfile.write("[\n")

try:
    for row in reader:
        row["day"] = int(row["day"])
        row["inRH"] = int(row["inRH"])
        row["unixtime"] = int(row["unixtime"])
        row["inTempC"] = float(row["inTempC"])
        row["outTempC"] = float(row["outTempC"])
        row["inTempF"] = float(row["inTempF"])
        row["outDewptF"] = float(row["outDewptF"])
        row["outTempF"] = float(row["outTempF"])
        row["pressure"] = float(row["pressure"])
        row["avgWind"] = float(row["avgWind"])
        row["gustWind"] = float(row["gustWind"])
        json.dump(row, jsonfile)
        jsonfile.write(',\n')
        row_number += 1
except:
    print(row_number)

# trailing bracket
jsonfile.write("]\n")

csvfile.close()
jsonfile.close()
