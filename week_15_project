# import the AWS SDK for Python
import boto3
# import the json modules
import json

# define the lambda handler
def lambda_handler(event, context):
    client = boto3.client('sqs')
    response = client.create_queue(
        QueueName='queue_created_by_lambda')
    
# define sucess response   
    return { 
        'statusCode': 200,
        'body': json.dumps("Queue has been created")
    }
