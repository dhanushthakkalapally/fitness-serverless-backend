import json
import boto3
import datetime
import os

# {
#     "date": "2022-07-16",
#     "nutritional_info": {
#         "breakfast": {"items": [{"name": "string", "calories": "number"}]}, 
#         "lunch": {"items": [{"name": "string", "calories": "number"}]}, 
#         "dinner": {"items": [{"name": "string", "calories": "number"}]}, 
#         "snacks": {"items": [{"name": "string", "calories": "number"}]}
#     } 
# }

region_name = os.environ["REGION_NAME"]
client = boto3.client("dynamodb", region_name=region_name)
TABLE_NAME = os.environ.get("TABLE_NAME") 

def lambda_handler(message, context):
    user_uuid = message["pathParameters"]["user_uuid"]
    date = message["pathParameters"]["date"]
    # user_uuid = message["requestContext"]["authorizer"]["claims"]["sub"]
    # request_body = json.loads(message["body"])
    # date = request_body.get("date", str(datetime.datetime.now().date()))
    # calorie_dict = {"morning": {"SS": ["eggs"]}, "lunch": {"SS": ["milk"]}, "dinner": {"SS": ["water"]}, "user_uuid": {"S": user_uuid}, "date": {"S": date}}
    
    # response = client.put_item(TableName = TABLE_NAME, Item=calorie_dict)

    return {
        "statusCode": 201,
        "headers": {},
        "body": json.dumps({"user_uuid": user_uuid, "date": date})
    }