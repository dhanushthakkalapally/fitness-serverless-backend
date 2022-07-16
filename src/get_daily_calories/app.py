import json


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