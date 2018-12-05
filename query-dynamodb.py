import boto3
from boto3.dynamodb.conditions import Key
import datetime
import re
from termcolor import colored

def valid_date(datestring):
    try:
        date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
        if date_pattern.match(datestring) and datetime.datetime.strptime(datestring, '%Y-%m-%d'):
            return True
    except ValueError:
        return False


datestr = input("What date (yyyy-mm-dd):  ")

if(valid_date(datestr)):
    resource = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    table = resource.Table('WeatherData')

    lst = [] # will contain a list of lists
    response = table.query(KeyConditionExpression=Key('yyyy-mm-dd').eq(datestr))
    for item in response['Items']:
        lst.append([item['time'] ,int(item['unixtime']), float(item['outTempF'])])

    for entry in lst:
        print(entry)
else:
    print(colored("\nDate format incorrect or not a valid calendar date!\n", "red"))
    exit()
