#Enabling VIM emulator(In tools option) might affect the highlighting and delete button.

import csv
import boto3

with open('credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

face_201103 = '201103.jpg'
face_jaychou2 = 'inputjaychou2.jpg'


client = boto3.client('rekognition',
                      aws_access_key_id = access_key_id,
                      aws_secret_access_key = secret_access_key,
                      region_name = 'us-east-2')

response = client.detect_faces(
    Image={
        'S3Object': {
            'Bucket': 'facer-source',
            'Name': face_201103,
        },
    },
    Attributes=[
        'ALL'
    ]

)

print(response)
