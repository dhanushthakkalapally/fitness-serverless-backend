import json
import boto3
import datetime
import os

region_name = os.environ["REGION_NAME"]
client = boto3.client("dynamodb", region_name=region_name)
TABLE_NAME = os.environ.get("TABLE_NAME") 

def lambda_handler(message, context):
    user_uuid = message["requestContext"]["authorizer"]["claims"]["sub"]
    request_body = json.loads(message["body"])
    date = request_body.get("date", str(datetime.datetime.now().date()))
    calorie_dict = {"morning": {"SS": ["eggs"]}, "lunch": {"SS": ["milk"]}, "dinner": {"SS": ["water"]}, "user_uuid": {"S": user_uuid}, "date": {"S": date}}
    
    response = client.put_item(TableName = TABLE_NAME, Item=calorie_dict)
    
    print(response)

    return {
        "statusCode": 201,
        "headers": {},
        "body": json.dumps(response)
    }