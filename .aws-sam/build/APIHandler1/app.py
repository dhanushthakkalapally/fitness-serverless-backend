import json
import boto3

def lambda_handler(event, context):
    username = event["requestContext"]["authorizer"]["claims"]["preferred_username"]
    
    return {
        'statusCode': 200,
        'body': json.dumps({"message": "welcome %s"%username}),
        "headers": {
            "Content-type": "application/json"
        }
    }


def lambda_handler1(event, context):    
    return {
        'statusCode': 200,
        'body': json.dumps({"message": "welcome from the new lambda handler"}),
        "headers": {
            "Content-type": "application/json"
        }
    }