#Enabling VIM emulator(In tools option) might affect the highlighting and delete button.
#0212
#Combine howdy.compare and testhowdy.compare
#take note on exit(number), eliminate unneccessary sections with local models and etc
#

# Import required modules
import time
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

# Try to import dlib and give a nice error if we can't
# Add should be the first point where import issues show up

id = "id"
timings = {
	"st": time.time()
}
def match():
    id = 'in match'
    try:
        import dlib
    except ImportError as err:
        print(err)

        print("\nCan't import the dlib module, check the output of")
        print("pip3 show dlib")
        sys.exit(1)

    # Get the absolute path to the current directory
    path = os.path.abspath(__file__ + "/..")

    # Test if at lest 1 of the data files is there and abort if it's not
    # if not os.path.isfile(path + "/../dlib-data/shape_predictor_5_face_landmarks.dat"):
    if not os.path.isfile(path + "/dlib-data/shape_predictor_5_face_landmarks.dat"):
        print("Data files have not been downloaded, please run the following commands:")
        print("\n\tcd " + os.path.realpath(path + "/../dlib-data"))
        print("\tsudo ./install.sh\n")
        sys.exit(1)

    # Read config from disk
    config = configparser.ConfigParser()
    # config.read(path + "/../config.ini")
    config.read(path + "/config.ini")

    if not os.path.exists(config.get("video", "device_path")):
        print("Camera path is not configured correctly, please edit the 'device_path' config value.")
        sys.exit(1)

    use_cnn = config.getboolean("core", "use_cnn", fallback=False)
    if use_cnn:
        face_detector = dlib.cnn_face_detection_model_v1(path + "/../dlib-data/mmod_human_face_detector.dat")
    else:
        face_detector = dlib.get_frontal_face_detector()

    pose_predictor = dlib.shape_predictor(path + "/dlib-data/shape_predictor_5_face_landmarks.dat")
    face_encoder = dlib.face_recognition_model_v1(path + "/dlib-data/dlib_face_recognition_resnet_model_v1.dat")

    def stop(status):
        """Stop the execution and close video stream"""
        video_capture.release()
        sys.exit(status)

    if os.path.isfile('photo/student.jpg'):
        print ("Previous file exists")
        # os.remove('cli/photo/student.jpg')
        print('Cleared')
    else:
        print ("Previous file not exist")

    print("___________________________________")
    print("Welcome to Putra Future Classroom")

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

    print("\nFace recognition is activated. Please look straight to the camera")

    # Give the user time to read
    time.sleep(3)

    frames = 0
    timings["fr"] = time.time()

    dark_threshold = config.getfloat("video", "dark_threshold")
    timeout = config.getint("video", "timeout")
    # Loop through frames till we hit a timeout

    # if os.path.isfile('face10.jpg'):
    #     print ("File exist")
    #     os.remove('face10.jpg')
    #     print('One photo is removed')
    # else:
    #     print ("File not exist")
    #
    # def capture():
    #     print("\nFace found!")
    #     cv2.imwrite("face10.jpg", frame)



    # a = Timer(2.0, capture)

    while frames < 60:

        # Stop if we've exceded the time limit



        # Grab a single frame of video
        # Don't remove ret, it doesn't work without it
        ret, frame = video_capture.read()

        if frames == 1 and ret is False:
            print("Could not read from camera")
            exit(12)

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

        if frames > 50:
            stop(11)

        # Get all faces from that frame as encodings
        face_locations = face_detector(gsframe, 1)

        # If we've found at least one, we can continue
        if face_locations:
                print("\nFace detected! Authenticating...")
                cv2.imwrite("photo/student.jpg", frame)
                break



    video_capture.release()

    # If more than 1 faces are detected we can't know wich one belongs to the user
    if len(face_locations) > 1:
        print("Multiple faces detected, aborting")
        sys.exit(1)
    elif not face_locations:
        print("No face detected, aborting")
        sys.exit(1)

    with open('admin2_credentials.csv', 'r') as input:
        next(input)
        reader = csv.reader(input)
        for line in reader:
            access_key_id = line[2]
            secret_access_key = line[3]

    photo = 'photo/student.jpg'


    client = boto3.client('rekognition',
                          aws_access_key_id = access_key_id,
                          aws_secret_access_key = secret_access_key,
                          region_name = 'us-east-2')


    with open(photo, 'rb') as source_image:
        source_bytes = source_image.read()

    response = client.search_faces_by_image(
        CollectionId='c3',
        FaceMatchThreshold=90,

        Image={'Bytes': source_bytes},
        MaxFaces=5,
    )

    # print(response)
    if(response['FaceMatches'] == []):
        print("You are unidentified. Authentication failed.")
        sys.exit(1)

    elif(response['SearchedFaceConfidence'] > 90):
        print("Similarity: " + str(response['FaceMatches'][0]['Similarity']))
        print("Confidence: " + str(response['FaceMatches'][0]['Face']['Confidence']))
        print("Face ID: " + response['FaceMatches'][0]['Face']['FaceId'])
        authenticated_user = response['FaceMatches'][0]['Face']['ExternalImageId']


        # Substring is searched in 'eks for geeks'
        position = authenticated_user.find('-', 0)
        length = len(authenticated_user)

        matric = authenticated_user[0:position]
        name = authenticated_user[position + 1:length]
        fullname = name.replace("_", " ")

        print("Welcome, " + fullname + ". Enjoy learning!")

        stop(0)

    else:
        print("Authentication failed.")
        return "failed"




def test():
    print('testing function')

def tryf():
    print('trying function')

match()


# print("Hello, no function is invoked.")








