#Enabling VIM emulator(In tools option) might affect the highlighting and delete button.

import csv
import boto3

with open('/home/weijin/PycharmProjects/testhowdy/cli/admin2_credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]


client = boto3.client('rekognition',
                      aws_access_key_id = access_key_id,
                      aws_secret_access_key = secret_access_key,
                      region_name = 'us-east-2')

# response = client.create_collection(
#     CollectionId='c3'
# )
#
# print(response)

# response = client.describe_collection(
#     CollectionId='c3'
# )
# print(response)

#
# response = client.delete_collection(
#     CollectionId='c3'
# )
#
# print(response)
#
response = client.list_faces(
    CollectionId='c3'
)
print(response)

# response = client.delete_faces(
#     CollectionId='c3',
#     FaceIds=[
#     '06933047-eb4f-4cb1-a071-5e327ff89ead',
# '144700ad-aef6-422a-97fc-145b67e0cf77'
#     ]
# )
