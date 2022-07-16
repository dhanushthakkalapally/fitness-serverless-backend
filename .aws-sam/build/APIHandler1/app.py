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