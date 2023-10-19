# import the AWS SDK for Python
import boto3
# import the module to generate random numbers
import random
# import the json module 
import json

# define the Lambda handler function
def lambda_handler(event, context):
    random_number = (random.randint(0, 9)) #generate a random number between 0 and 9
    
    # create an SQS client 
    sqs = boto3.client('sqs')
    
    # send a message to the SQS queue that was created with the queue URL
    sqs.send_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/675901025615/queue_created_by_lambda',  # URL of the SQS queue
        MessageBody=str(random_number),  # Convert the random number to a string and use it as the message
    )
    
    # return a successful response 
    return {
        'statusCode': 200,
        'body': json.dumps(random_number)  # convert the random number into JSON format and use it as the message
    }
