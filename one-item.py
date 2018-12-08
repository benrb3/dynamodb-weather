import json
import pandas as pd
import sys

infile  = "/home/ben/tmp/sqlite3/one-item.csv"
outfile = "/home/ben/tmp/sqlite3/one-item.json"

def create_list_from_file(filepath):
    # check for missing values in *.csv file
    df = pd.read_csv(filepath)
    df = df.dropna(how='any',axis=0)
    if len(df) < 1:
        #print("Missing data in *.csv file")
        sys.exit(1) #error
    with open(filepath) as fh:
        next(fh) # skip first line
        data = fh.read()
    fh.close()
    lst = data.split(',')
    new_lst = []
    for item in lst:
        new_lst.extend(item.split()) # splits on a space, which breaks up 'timestring'
    return(new_lst)

def create_json_output(lst):
    return {
    "yyyy-mm-dd": {"S": lst[0]},
    "time":       {"S": lst[1]},
    "unixtime":   {"S": lst[2]},
    "inTempC":    {"S": lst[3]},
    "inTempF":    {"S": lst[4]},
    "outTempC":   {"S": lst[5]},
    "outTempF":   {"S": lst[6]},
    "pressure":   {"S": lst[7]},
    "inRH":       {"S": lst[8]},
    "outDewptF":  {"S": lst[9]},
    "avgWind":    {"S": lst[10]},
    "gustWind":   {"S": lst[11]}
    }

def write_json_to_file(dictionary):
    with open(outfile, "w") as fp:
        json.dump(dictionary, fp)


l = create_list_from_file(infile)
dct = create_json_output(l)
# write json dictionary to file
write_json_to_file(dct)
sys.exit(0) #success
