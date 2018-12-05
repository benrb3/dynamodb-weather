import pandas as pd
import boto3

filename = input("What is the filename? ")

df = pd.read_csv(filename, low_memory=False, skiprows=1)
df.columns = ["yyyy-mm-dd","time","unixtime","inTempC","inTempF","outTempC","outTempF","pressure","inRH","outDewptF","avgWind","gustWind"]

# convert all attributes to type 'string' for safety
for i in df.columns:
    df[i] = df[i].astype(str)

# create a dictionary
myl=df.T.to_dict().values()

#resource = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")
resource = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
table = resource.Table('WeatherData')
with table.batch_writer() as batch:
    for item in myl:
        batch.put_item(Item=item)
