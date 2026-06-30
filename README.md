Smart Image Recognition & Voice Generator
Project Overview
This serverless AWS project automatically analyzes images uploaded to Amazon S3, detects objects and labels using Amazon Rekognition, generates voice descriptions using Amazon Polly, and stores metadata in DynamoDB.

Architecture
S3 → Lambda → Rekognition → Polly → DynamoDB → S3

AWS Services Used
Amazon S3
AWS Lambda
Amazon Rekognition
Amazon Polly
Amazon DynamoDB
AWS IAM
Amazon CloudWatch
Workflow
Upload an image to an S3 bucket.
S3 triggers a Lambda function.
Lambda sends the image to Amazon Rekognition.
Rekognition detects labels from the image.
Lambda stores image metadata in DynamoDB.
Lambda sends label information to Amazon Polly.
Polly generates an MP3 audio description.
The MP3 file is stored in the S3 bucket.
Technologies
Python
Boto3
AWS Cloud Services
Example Output
Image: dog.jpg

Detected Labels:

Dog
Pet
Animal
Generated Audio: "This image contains Dog, Pet, Animal."

Author
Sanika Shingan
