import json
import boto3
import os

region_name = os.environ["REGION_NAME"]
dynamodb = boto3.resource("dynamodb", region_name=region_name)
TABLE_NAME = os.environ.get("TABLE_NAME") 
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(message, context):
    user_uuid = message["pathParameters"]["user_uuid"]
    date = message["pathParameters"]["date"]

    response = table.get_item(
        Key={
            'user_uuid': user_uuid,
            'date': date
        }
    )

    return {
        "statusCode": 200,
        "headers": {},
        "body": json.dumps(response["Items"])
    }