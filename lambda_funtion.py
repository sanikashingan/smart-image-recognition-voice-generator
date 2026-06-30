import boto3
from datetime import datetime

# AWS Clients
rekognition = boto3.client('rekognition')
polly = boto3.client('polly')
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

TABLE_NAME = "ImageMetadata02"

def lambda_handler(event, context):

    # Get bucket name
    bucket = event['Records'][0]['s3']['bucket']['name']

    # Get uploaded image name
    image_key = event['Records'][0]['s3']['object']['key']

    print("Image Uploaded:", image_key)

    # Detect labels using Rekognition
    response = rekognition.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': image_key
            }
        },
        MaxLabels=5
    )

    labels = []

    for label in response['Labels']:
        labels.append(label['Name'])

    print("Detected Labels:", labels)

    # Create sentence for Polly
    speech_text = "This image contains " + ", ".join(labels)

    print("Speech Text:", speech_text)

    # Generate voice using Polly
    polly_response = polly.synthesize_speech(
        Text=speech_text,
        OutputFormat='mp3',
        VoiceId='Joanna'
    )

    # Audio file name
    audio_key = image_key.split('.')[0] + ".mp3"

    # Save MP3 to S3
    s3.put_object(
        Bucket=bucket,
        Key="audio/" + audio_key,
        Body=polly_response['AudioStream'].read(),
        ContentType='audio/mpeg'
    )

    print("Audio File Created:", audio_key)

    # Save metadata to DynamoDB
    table = dynamodb.Table(TABLE_NAME)

    table.put_item(
        Item={
            'ImageName': image_key,
            'Labels': ", ".join(labels),
            'UploadTime': str(datetime.utcnow()),
            'AudioFile': audio_key
        }
    )

    print("Metadata Saved")

    return {
        'statusCode': 200,
        'body': 'Success'
    }
