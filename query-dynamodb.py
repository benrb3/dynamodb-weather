import boto3
from boto3.dynamodb.conditions import Key

datestr = input("What date (yyyy-mm-dd):  ")
resource = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
table = resource.Table('WeatherData')

response = table.query(KeyConditionExpression=Key('yyyy-mm-dd').eq(datestr))
for item in response['Items']:
    print(item['yyyy-mm-dd'], ":", item['inRH'])
