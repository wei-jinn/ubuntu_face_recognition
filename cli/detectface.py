# Detect face and save as photo
# Import required modules

# import time
# import os
# import sys
# import json
# import configparser
# import builtins
# import cv2
# import numpy as np
# from threading import Timer
# import csv
# import boto3
# import dlib

# Try to import dlib and give a nice error if we can't
# Add should be the first point where import issues show up

# def detect():
#     msg = "No result yet"
    # try:
    #     import dlib
    # except ImportError as err:shell_exec('cd');
    #     print(err)
    #
    #     print("\nCan't import the dlib module, check the output of")
    #     print("pip3 show dlib")
    #     sys.exit(1)

    # Get the absolute path to the current directory
    # path = os.path.abspath(__file__ + "/..")
    #
    # # Test if at lest 1 of the data files is there and abort if it's not
    # if not os.path.isfile(path + "/../dlib-data/shape_predictor_5_face_landmarks.dat"):
    #     print("Data files have not been downloaded, please run the following commands:")
    #     print("\n\tcd " + os.path.realpath(path + "/../dlib-data"))
    #     print("\tsudo ./install.sh\n")
    #     sys.exit(1)
    #
    # # Read config from disk
    # config = configparser.ConfigParser()
    # config.read(path + "/../config.ini")
    #
    # if not os.path.exists(config.get("video", "device_path")):
    #     print("Camera path is not configured correctly, please edit the 'device_path' config value.")
    #     sys.exit(1)
    #
    # use_cnn = config.getboolean("core", "use_cnn", fallback=False)
    # if use_cnn:
    #     face_detector = dlib.cnn_face_detection_model_v1(path + "/../dlib-data/mmod_human_face_detector.dat")
    # else:
    #     face_detector = dlib.get_frontal_face_detector()
    #
    # pose_predictor = dlib.shape_predictor(path + "/../dlib-data/shape_predictor_5_face_landmarks.dat")
    # face_encoder = dlib.face_recognition_model_v1(path + "/../dlib-data/dlib_face_recognition_resnet_model_v1.dat")
    #
    # # if os.path.isfile('photo/detect.jpg'):
    # #     print ("Previous file exists")
    # #     os.remove('photo/detect.jpg')
    # #     print('Cleared')
    # # else:
    # #     print ("Previous file not exist")
    #
    #
    # print("___________________________________")
    # print("Detecting face")
    #
    # # Start video capture on the IR camera through OpenCV
    # video_capture = cv2.VideoCapture(config.get("video", "device_path"))
    #
    # # Set the frame width and height if requested
    # fw = config.getint("video", "frame_width", fallback=-1)
    # fh = config.getint("video", "frame_height", fallback=-1)
    # if fw != -1:
    #     video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, fw)
    #
    # if fh != -1:
    #     video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, fh)
    #
    # # Request a frame to wake the camera up
    # video_capture.grab()
    #
    # print("\nWe are taking photo of your face now. Please look straight to the camera.")
    #
    # # Give the user time to read
    # time.sleep(3)
    #
    # frames = 0
    # dark_threshold = config.getfloat("video", "dark_threshold")
    #
    # # Loop through frames till we hit a timeout
    #
    #
    # #
    # # def capture():
    # #     print("\nFace found!")
    # #     cv2.imwrite("face10.jpg", frame)
    #
    # # a = Timer(2.0, capture)
    #
    # while frames < 20:
    #     # Grab a single frame of video
    #     # Don't remove ret, it doesn't work without it
    #     ret, frame = video_capture.read()
    #     gsframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #
    #     # Create a histogram of the image with 8 values
    #     hist = cv2.calcHist([gsframe], [0], None, [8], [0, 256])
    #     # All values combined for percentage calculation
    #     hist_total = np.sum(hist)
    #
    #     # If the image is fully black or the frame exceeds threshold,
    #     # skip to the next frame
    #     if hist_total == 0 or (hist[0] / hist_total * 100 > dark_threshold):
    #         continue
    #
    #     frames += 1
    #
    #     # Get all faces from that frame as encodings
    #     face_locations = face_detector(gsframe, 1)
    #
    #     # If we've found at least one, we can continue
    #     if len(face_locations) == 1:
    #         print("\nFace detected! Saving as jpg...")
    #         cv2.imwrite("/opt/lampp/htdocs/awssdk/public/storage/input_image/detect.jpg", frame)
    #         msg = "A face is detected and saved"
    #         break
    #     elif len(face_locations) > 1:
    #         print("Multiple faces detected, retrying for attempt " + str(frames))
    #         msg = "Failed to capture a face"
    #         continue
    #     elif not face_locations:
    #         print("No face detected, retrying for attempt " + str(frames))
    #         msg = "Failed to capture a face"
    #         continue
    #
    # video_capture.release()
    #
    # print(msg)
    # return msg



# If more than 1 faces are detected we can't know wich one belongs to the user
print("Get photo here")