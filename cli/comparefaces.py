#Enabling VIM emulator(In tools option) might affect the highlighting and delete button.

#kinesis video streaming getting started: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/getting-started.html
#accessKey for admin : 7VaXfdb9tq5SVbEvLSsennnJ4LsTdRkySlE2c5sO
#Amazon Resource Name for role rekognition_accesstoKinesis: arn:aws:iam::681072845145:role/rekognition_accesstoKinesis
# (FacerStream) Kinesis Video StreamARN = arn:aws:kinesisvideo:eu-west-1:681072845145:stream/FacerStream/1575019165354
# (AmazonRekognition_facer) Kinesis Data Stream ARNarn = aws:kinesis:eu-west-1:681072845145:stream/AmazonRekognition_facer

import csv
import boto3

with open('admin2_credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

target_img = '201105.jpg'
source_img = 'if_jj07.jpg'


client = boto3.client('rekognition',
                      aws_access_key_id = access_key_id,
                      aws_secret_access_key = secret_access_key,
                      region_name = 'us-east-2')
                      # region_name = 'eu-west-1')


response = client.compare_faces(
    SourceImage={
        'S3Object': {
            'Bucket': 'facer-source',
            'Name': source_img,
        },
    },
    TargetImage={
        'S3Object': {
            'Bucket': 'facer-source',
            'Name': target_img,
        },
    },
    SimilarityThreshold=90

)

for key, value in response.items():
    if key in ('FaceMatches', 'UnmatchedFaces'):
        print(key)
        for att in value:
            print(att)

