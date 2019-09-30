import boto3

class Dynamo:
    dynamoDB = None
    clientDynamoDB = None

    def __init__(self):
        self.dynamoDB = boto3.resource('dynamodb')
        self.clientDynamoDB = boto3.client('dynamodb')