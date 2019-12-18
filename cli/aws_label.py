#Enabling VIM emulator(In tools option) might affect the highlighting and delete button.

import csv
import boto3

with open('credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

photo = 'photo/hab.jpg'
photo2 = 'hab.jpg'
photo3 = 'city.jpg'
bucket = 'facer-source'

client = boto3.client('rekognition',
                      aws_access_key_id = access_key_id,
                      aws_secret_access_key = secret_access_key,
                      region_name = 'us-east-2')


with open(photo, 'rb') as source_image:
    source_bytes = source_image.read()

# get source from local photo folder.
# response = client.detect_labels(Image={'Bytes': source_bytes},
#                                 MaxLabels=5,
#                                 MinConfidence=90)
#
# print(response)
# print(access_key_id, secret_access_key)

# get source from s3 bucket
response = client.detect_labels(
    Image={
        'S3Object': {
            'Bucket': bucket,
            'Name': photo2,
        },
    },
    MaxLabels=3,
    MinConfidence=80,
)

print(response)

# print("Hello World")
#


# number = 90
#
# if(number < 10):
#     print("the number is too small")
# else:
#     print("The number is too big")
#
#
# count = 0
#
# while(count < 10):
#     print("counting ", count, " good attempt")
#     count +=2
