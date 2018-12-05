import boto3

def get_dynamodb_resource():
    #rds = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")
    resource = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    return resource

def create_table():
    dynamodb = get_dynamodb_resource()
    try:
        table = dynamodb.create_table(
            TableName='WeatherData',
            KeySchema=[
                 {'AttributeName': 'yyyy-mm-dd', 'KeyType': 'HASH'},
                 {'AttributeName': 'unixtime',   'KeyType': 'RANGE'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'yyyy-mm-dd', 'AttributeType': 'S'},
                {'AttributeName': 'unixtime',    'AttributeType': 'S'}
            ],
            ProvisionedThroughput={'ReadCapacityUnits':5, 'WriteCapacityUnits': 250}
        )
        print('created table {}.'.format(table))

        # Wait until the table exists.
        table.meta.client.get_waiter('table_exists').wait(TableName='WeatherData')

        # print out some data about the new table
        print(table.item_count)

    except AssertionError as e:
            raise e

# Call the function to create the table
create_table()
