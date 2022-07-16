import json
import boto3
import os

# {
    # now we only support four categories, but in future we may support more :) we don't know yet
#     "consumptions": {
#         "breakfast": {"items": [{"name": "string", "calories": "number"}]}, 
#         "lunch": {"items": [{"name": "string", "calories": "number"}]}, 
#         "dinner": {"items": [{"name": "string", "calories": "number"}]}, 
#         "snacks": {"items": [{"name": "string", "calories": "number"}]}
#     } 
# }

region_name = os.environ["REGION_NAME"]
dynamodb = boto3.resource("dynamodb", region_name=region_name)
TABLE_NAME = os.environ.get("TABLE_NAME") 
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(message, context):
    user_uuid = message["pathParameters"]["user_uuid"]
    date = message["pathParameters"]["date"]
    if user_uuid and date:
        #TODO: make sure user doesn't send the date from the future and also actually sends the date
        #TODO: Also check if the users is valid in the cognito before creating the record
        #TODO: Validate the schema of the data that we are receiving
        request_body = json.loads(message["body"])
        daily_calorie_consumptions = {"user_uuid": user_uuid,
                                      "date": date, 
                                      "consumptions": {}, 
                                      "total_calories": 0}
        
        consumptions = request_body.get("consumptions", {})
        for consumption_type in consumptions.keys():
            if consumption_type in ["breakfast", "dinner", "lunch", "snacks"]:
                consumption = consumptions[consumption_type]
                calories = 0
                items = consumption["items"]
                for item in items:
                    calories += item["calories"]
                consumption["meal_calories"] = calories
                daily_calorie_consumptions["consumptions"][consumption_type] = consumption 
                daily_calorie_consumptions["total_calories"] += calories 

        table.put_item(Item=daily_calorie_consumptions)

    else:
        return {
            "statusCode": 400,
            "headers": {"application/json"},
            "body": json.dumps({"body": "invalid Request"})
        }
    return {
        "statusCode": 201,
        "headers": {}
    }