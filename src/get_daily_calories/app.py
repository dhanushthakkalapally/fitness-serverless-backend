import json, decimal
import boto3
import os

region_name = os.environ["REGION_NAME"]
dynamodb = boto3.resource("dynamodb", region_name=region_name)
TABLE_NAME = os.environ.get("TABLE_NAME") 
table = dynamodb.Table(TABLE_NAME)

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

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
        "body": json.dumps(response["Item"], cls=DecimalEncoder, indent=4)
    }