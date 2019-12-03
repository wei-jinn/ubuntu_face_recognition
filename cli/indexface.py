#Enabling VIM emulator(In tools option) might affect the highlighting and delete button.

import csv
import boto3

with open('admin2_credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

photo = 'photo/student.jpg'
eid = "JiaJing"


client = boto3.client('rekognition',
                      aws_access_key_id = access_key_id,
                      aws_secret_access_key = secret_access_key,
                      region_name = 'us-east-2')


with open(photo, 'rb') as source_image:
    source_bytes = source_image.read()

response = client.index_faces(
    CollectionId='c2',
    DetectionAttributes=[
        'DEFAULT'
    ],
    Image={'Bytes': source_bytes},
    ExternalImageId = eid,
    MaxFaces=1,
)

if(response):
    print("Face Added Successfully.")