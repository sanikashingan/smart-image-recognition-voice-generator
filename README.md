# smart-image-recognition-voice-generator
# Smart Image Recognition & Voice Generator

## Project Overview

This serverless AWS project automatically analyzes images uploaded to Amazon S3, detects objects and labels using Amazon Rekognition, generates voice descriptions using Amazon Polly, and stores metadata in DynamoDB.

## Architecture

S3 → Lambda → Rekognition → Polly → DynamoDB → S3

## AWS Services Used

* Amazon S3
* AWS Lambda
* Amazon Rekognition
* Amazon Polly
* Amazon DynamoDB
* AWS IAM
* Amazon CloudWatch

## Workflow

1. Upload an image to an S3 bucket.
2. S3 triggers a Lambda function.
3. Lambda sends the image to Amazon Rekognition.
4. Rekognition detects labels from the image.
5. Lambda stores image metadata in DynamoDB.
6. Lambda sends label information to Amazon Polly.
7. Polly generates an MP3 audio description.
8. The MP3 file is stored in the S3 bucket.

## Technologies

* Python
* Boto3
* AWS Cloud Services

## Example Output

Image: dog.jpg

Detected Labels:

* Dog
* Pet
* Animal

Generated Audio:
"This image contains Dog, Pet, Animal."

## Author

Dinesh Ghule
### Architecture
![Architecture](https://github.com/Dinu737/smart-image-recognition-voice-generator/blob/165760fe896d8e39f2ed446077ac6dd78e7af866/architecture.jpg.png)

### DynamoDb
![DynamoDB](https://github.com/Dinu737/smart-image-recognition-voice-generator/blob/e868b2eb48949b186b9dc9698d18cbfdb768bb80/dynamoDB.jpg.png)

### Lambda Function Code
![lambda_function](https://github.com/Dinu737/smart-image-recognition-voice-generator/blob/24736e185784a6aeb4d1400681570a42f3ed1003/lambdacode.jpg.png)

### CloudWatch Detection 
![CloudWatch](https://github.com/Dinu737/smart-image-recognition-voice-generator/blob/3c8288f1a91e086c6207f8306325800bf19fa01d/cloudwatch.jpg.png)

### Final Output in mp3 file 
![mp3](https://github.com/Dinu737/smart-image-recognition-voice-generator/blob/7dc2915714a3ed987b54a06932f4f05d54732865/mp3output.jpg.png)
