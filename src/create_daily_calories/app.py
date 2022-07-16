import json
import boto3


def lambda_handler(message, context):

    print(message);

    return {
        "statudCode": 200,
        "headers": {},
        "body": json.dumps(message["body"])
    }