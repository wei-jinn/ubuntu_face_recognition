#Enabling VIM emulator(In tools option) might affect the highlighting and delete button.
#0212
#Combine howdy.compare and testhowdy.compare
#take note on exit(number), eliminate unneccessary sections with local models and etc
#

# Import required modules
import signal
import time
from datetime import datetime
import os
import sys
import json
import configparser
import builtins
import cv2
import numpy as np
from threading import Timer
import csv
import boto3
# to import the scripts from different directory
import sys
import requests
import dlib

# Try to import dlib and give a nice error if we can't
# Add should be the first point where import issues show up

authenticated_user = "authenticated_user"

# try:
#     import dlib
# except ImportError as err:
#     print(err)
#
#     print("\nCan't import the dlib module, check the output of")
#     print("pip3 show dlib")
#     sys.exit(1)

# Get the absolute path to the current directory
path = os.path.abspath(__file__ + "/..")

# Test if at lest 1 of the data files is there and abort if it's not
if not os.path.isfile(path + "/../dlib-data/shape_predictor_5_face_landmarks.dat"):
    print("Data files have not been downloaded, please run the following commands:")
    print("\n\tcd " + os.path.realpath(path + "/../dlib-data"))
    print("\tsudo ./install.sh\n")
    sys.exit(1)

# Read config from disk
config = configparser.ConfigParser()
config.read(path + "/../config.ini")

if not os.path.exists(config.get("video", "device_path")):
    print("Camera path is not configured correctly, please edit the 'device_path' config value.")
    sys.exit(1)

use_cnn = config.getboolean("core", "use_cnn", fallback=False)
if use_cnn:
    face_detector = dlib.cnn_face_detection_model_v1(path + "/../dlib-data/mmod_human_face_detector.dat")
else:
    face_detector = dlib.get_frontal_face_detector()

pose_predictor = dlib.shape_predictor(path + "/../dlib-data/shape_predictor_5_face_landmarks.dat")
face_encoder = dlib.face_recognition_model_v1(path + "/../dlib-data/dlib_face_recognition_resnet_model_v1.dat")

def stop(status):
    """Stop the execution and close video stream"""
    video_capture.release()
    sys.exit(status)

if os.path.isfile('/home/weijin/PycharmProjects/testhowdy/cli/photo/facialexpression.jpg'):
    print ("Previous file exists")
    os.remove('/home/weijin/PycharmProjects/testhowdy/cli/photo/facialexpression.jpg')
    print('Cleared')
else:
    print ("Previous file not exist")

print("___________________________________")


# Start video capture on the IR camera through OpenCV
video_capture = cv2.VideoCapture(config.get("video", "device_path"))

# Set the frame width and height if requested
fw = config.getint("video", "frame_width", fallback=-1)
fh = config.getint("video", "frame_height", fallback=-1)
if fw != -1:
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, fw)

if fh != -1:
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, fh)

# Request a frame to wake the camera up
video_capture.grab()


# Give the user time to read
time.sleep(0)

frames = 0

dark_threshold = config.getfloat("video", "dark_threshold")
# timeout = config.getint("video", "timeout")
# Loop through frames till we hit a timeout

# start recognition
while True:
    # Grab a single frame of video
    # Don't remove ret, it doesn't work without it

    ret, frame = video_capture.read()
    gsframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Create a histogram of the image with 8 values
    hist = cv2.calcHist([gsframe], [0], None, [8], [0, 256])
    # All values combined for percentage calculation
    hist_total = np.sum(hist)

    # If the image is fully black or the frame exceeds threshold,
    # skip to the next frame
    if hist_total == 0 or (hist[0] / hist_total * 100 > dark_threshold):
        continue

    frames += 1
    print(frames)

    # Get all faces from that frame as encodings
    face_locations = face_detector(gsframe, 1)

    # If we've found at least one, we can continue
    if len(face_locations)==1:
        print("\nFace detected! Authenticating...")
        cv2.imwrite("/home/weijin/PycharmProjects/testhowdy/cli/photo/student.jpg", frame)
        break
    elif len(face_locations) > 1:
        print("Multiple faces detected, retrying")
        continue
    elif not face_locations:
        print("No face detected, retrying")
        continue




# If more than 1 faces are detected we can't know wich one belongs to the user

with open('/home/weijin/PycharmProjects/testhowdy/cli/admin2_credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

photo = '/home/weijin/PycharmProjects/testhowdy/cli/photo/student.jpg'

client = boto3.client('rekognition',
                      aws_access_key_id=access_key_id,
                      aws_secret_access_key=secret_access_key,
                      region_name='us-east-2')

with open(photo, 'rb') as source_image:
    source_bytes = source_image.read()

response = client.search_faces_by_image(
    CollectionId='c3',
    FaceMatchThreshold=90,

    Image={'Bytes': source_bytes},
    MaxFaces=5,
)

# print(response)
if (response['FaceMatches'] == []):
    print("You are unidentified. Authentication failed.")
    sys.exit(1)

elif (response['SearchedFaceConfidence'] > 99):
    print("Similarity: " + str(response['FaceMatches'][0]['Similarity']))
    print("Confidence: " + str(response['FaceMatches'][0]['Face']['Confidence']))
    print("Face ID: " + response['FaceMatches'][0]['Face']['FaceId'])
    authenticated_user = response['FaceMatches'][0]['Face']['ExternalImageId']

    # Substring is searched in 'eks for geeks'
    position = authenticated_user.find('-', 0)
    length = len(authenticated_user)

    matric = int(authenticated_user[0:position])
    name = authenticated_user[position + 1:length]
    fullname = name.replace("_", " ")

    print("Welcome, " + fullname + ". Enjoy learning!")
    # return authenticated_user

else:
    print("Authentication failed.")
    # return "failed"

video_capture.release()
# video_capture.grab()
pid = 0

def receive_signal(signum, stack):
    print ('Received:', signum)
    print("I got your signal, let me sleep awhile")
    video_capture.release()
    signal.pause()
    # time.sleep(20)


def signal_start(signum, stack):

    print("Let's go back to work")
    time.sleep(1)




signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, signal_start)

try:
        while True:

            # while frames < 60:
            # Grab a single frame of video
            # Don't remove ret, it doesn't work without it

            video_capture = cv2.VideoCapture(config.get("video", "device_path"))
            print(video_capture)
            # Set the frame width and height if requested
            fw = config.getint("video", "frame_width", fallback=-1)
            fh = config.getint("video", "frame_height", fallback=-1)
            if fw != -1:
                video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, fw)

            if fh != -1:
                video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, fh)


            video_capture.grab()
            ret, frame = video_capture.read()
            # gsframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Create a histogram of the image with 8 values
            hist = cv2.calcHist([frame], [0], None, [8], [0, 256])
            # All values combined for percentage calculation
            hist_total = np.sum(hist)

            # If the image is fully black or the frame exceeds threshold,
            # skip to the next frame
            if hist_total == 0 or (hist[0] / hist_total * 100 > dark_threshold):
                continue

            frames += 1

            # Get all faces from that frame as encodings
            face_locations = face_detector(frame, 1)

            # If we've found at least one, we can continue
            if face_locations:
                    print("\nFace detected! Analysing...")
                    print(frames)
                    cv2.imwrite("/home/weijin/PycharmProjects/testhowdy/cli/photo/facialexpression.jpg", frame)
                    dateTimeObj = datetime.now()

            else:
                print("No face detected.")
                print(frames)
                video_capture.release()
                continue



        # If more than 1 faces are detected we can't know wich one belongs to the user
        # if len(face_locations) > 1:
        #     print("Multiple faces detected, aborting")
        #     sys.exit(1)
        # elif not face_locations:
        #     print("No face detected, aborting")
        #     sys.exit(1)

            video_capture.release()

            with open('/home/weijin/PycharmProjects/testhowdy/cli/admin2_credentials.csv', 'r') as input:
                next(input)
                reader = csv.reader(input)
                for line in reader:
                    access_key_id = line[2]
                    secret_access_key = line[3]

            photo = '/home/weijin/PycharmProjects/testhowdy/cli/photo/facialexpression.jpg'


            client = boto3.client('rekognition',
                                  aws_access_key_id = access_key_id,
                                  aws_secret_access_key = secret_access_key,
                                  region_name = 'us-east-2')


            with open(photo, 'rb') as source_image:
                source_bytes = source_image.read()


            response = client.detect_faces(
                Image={
                    'Bytes': source_bytes,

                },
                Attributes=[
                    'ALL',
                ]
            )


            def Merge(dict1, dict2):
                return (dict2.update(dict1))

            def bubbleSort(arr):
                n = len(arr)

                # Traverse through all array elements
                for i in range(n):

                    # Last i elements are already in place
                    for j in range(0, n - i - 1):

                        # traverse the array from 0 to n-i-1
                        # Swap if the element found is greater
                        # than the next element
                        if arr[j]['Confidence'] > arr[j + 1]['Confidence']:
                            arr[j], arr[j + 1] = arr[j + 1], arr[j]

            if(response):
                emotions = response['FaceDetails'][0]['Emotions']

                bubbleSort(emotions)
                for i in range(len(emotions) - 1, -1, -1):
                    print((emotions[i]['Type']).lower() + " : " + str(round(emotions[i]['Confidence'],2)))
                print(dateTimeObj)


                # data = {'student_id':matric,
                #         (emotions[0]['Type']).lower(): round(emotions[0]['Confidence'],2),
                #         (emotions[1]['Type']).lower(): round(emotions[1]['Confidence'],2),
                #         (emotions[2]['Type']).lower(): round(emotions[2]['Confidence'],2),
                #         (emotions[3]['Type']).lower(): round(emotions[3]['Confidence'],2),
                #         (emotions[4]['Type']).lower(): round(emotions[4]['Confidence'],2),
                #         (emotions[5]['Type']).lower(): round(emotions[5]['Confidence'],2),
                #         (emotions[6]['Type']).lower(): round(emotions[6]['Confidence'],2),
                #         (emotions[7]['Type']).lower(): round(emotions[7]['Confidence'],2),
                #         }
                #
                #
                # print(data)



                # for x in emotions:
                #     print(x['Type'] + " : " + str(round(x['Confidence'],2)))
                # print(emotions[0]['Type'])
                # print("Time taken : " + str(dateTimeObj))
                # time = {'Timetaken' : str(dateTimeObj)}
                # obj = [emotions,time]
                #
                # print(obj)
                # print(authenticated_user)

                # # data to be sent to api
                # data = {'api_dev_key': API_KEY,
                #         'api_option': 'paste',
                #         'api_paste_code': source_code,
                #         'api_paste_format': 'python'}
                #
                # sending post request and saving response as response object

                # r = requests.post(url='https://pure-headland-78653.herokuapp.com/api/resources/emotion', data=data)
                # print(r)

                # g = requests.get(url='https://pure-headland-78653.herokuapp.com/api/resources/emotion')
                # getdata = g.json()
                # print(getdata)



                if cv2.waitKey(1) != -1:
                    raise KeyboardInterrupt()


            # if(response):
            #     print(response['FaceDetails'][0]['Emotions'])
except KeyboardInterrupt:
    # Let the user know we're stopping
    # print("\nClosing window")
    print("Closing")
    video_capture.release()
    sys.exit(0)


















