import time
from datetime import datetime

import requests
import os
# import sys
# sys.path.insert(0, '/home/weijin/PycharmProjects/')
# from testhowdy import testpause
#
# testpause.stop()
# _______________________________________________________________________________________________
# dateTimeObj = datetime.now()
#
# -------------------------------Doing Bubble Sorting----------------------------------------------
# def bubbleSort(arr):
#     n = len(arr)
#
#     # Traverse through all array elements
#     for i in range(n):
#
#         # Last i elements are already in place
#         for j in range(0, n - i - 1):
#
#             # traverse the array from 0 to n-i-1
#             # Swap if the element found is greater
#             # than the next element
#             if arr[j]['Confidence'] > arr[j + 1]['Confidence']:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#
# arr = [{'Type': 'CALM', 'Confidence': 64}, {'Type': 'ANGRY', 'Confidence': 0.07},  {'Type': 'DISGUSTED', 'Confidence': 0.06}]
#
# # print(arr[0]['Type'])
# bubbleSort(arr)
#
# print("Sorted array is:")
# for i in range(len(arr)-1,-1,-1):
#     print(i)
#     print( arr[i]),
#
# -------------------------------Doing Data Merging----------------------------------------------
# print(dateTimeObj)
#
# arr.join(dateTimeObj)
#

# Python code to merge dict using update() method
# def Merge(dict1, dict2):
#     return (dict2.update(dict1))
#
# # Driver code
# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}
#
# # This return None
# Merge(dict1, dict2)
# print(dict2)
#
# -------------------------------Doing request----------------------------------------------

# import requests
# userdata = {"name": "Yonex Shoes", "quantity":"10"}
# resp = requests.post('http://awssdk.test:3000/getpythondata', params=userdata)

# -------------------------------External ID trimming----------------------------------------------
# word = '1-Chiew_Jia_Jing:184471'
#
# # Substring is searched in 'eks for geeks'
# position = word.find('-', 0)
# length = len(word)
# print(position)
# print(length)
# position_matric = word.find(':',0)
#
# uid = word[0:position]
# name = word[position+1:position_matric]
# matric = word[position_matric+1:length]
# fullname = name.replace("_", " ")
# print("_________________________")
# print(uid)
# print(fullname)
# print(matric)

# -------------------------------External ID trimming----------------------------------------------
# for i in range(len(emotions) - 1, -1, -1):
                #     print(emotions[i]['Type'] + " : " + str(round(emotions[i]['Confidence'],2)) + "%")
                # for x in emotions:
                #     print(x['Type'] + " : " + str(round(x['Confidence'],2)))
                # print(emotions[0]['Type'])
                # print("Time taken : " + str(dateTimeObj))str(dateTimeObj)
#
# arr = [{'Type': 'FEAR', 'Confidence': 0.006524436175823212}, {'Type': 'HAPPY', 'Confidence': 0.023475509136915207}, {'Type': 'ANGRY', 'Confidence': 0.057014573365449905}, {'Type': 'SURPRISED', 'Confidence': 0.06289278715848923}, {'Type': 'DISGUSTED', 'Confidence': 0.06303147971630096}, {'Type': 'CONFUSED', 'Confidence': 0.45292866230010986}, {'Type': 'SAD', 'Confidence': 0.501514196395874}, {'Type': 'CALM', 'Confidence': 98.83262634277344}]
#
# matric = 184471
# datetime = dateTimeObj
#
# emotions = [{'matric': matric}]
#
# print(arr)
#
# for i in range(len(arr) - 1, -1, -1):
#
#     emotions.append({arr[i]['Type'].lower() : str(round(arr[i]['Confidence'],2))})
#                 # for x in arr:
#                 #     print(x['Type'] + " : " + str(round(x['Confidence'],2))
#
# emotions.append({'created_at' : str(dateTimeObj)})
#
# print(emotions)

# -------------------------------Read, append and write files----------------------------------------------
#
# fullname = "Chiew Jia Jing"
# userid = "2"
#
# f = open('u.txt', "w+")
# f.write(fullname + "\n")
# f.close()
#
# a = open('u.txt', "a")
# a.write(userid)
# a.close()

#
# r = open('u.txt', "r")
# read = r.read()
# print(read)

# line_number = 2
#
# with open('u.txt', 'r') as filehandle:
#     current_line = 1
#     for line in filehandle:
#         if current_line == line_number:
#             userid = line
#             break
#         current_line += 1
#
# print(userid)

# -------------------------------Post data----------------------------------------------

# matric_data = {'student_id': '184471'
#                }
# #
# sendmatric = requests.post(url='http://127.0.0.1:8000/attendance', data=matric_data)
# print(sendmatric)

#
# uid_data = 1
# #
# senduid = requests.post(url='http://127.0.0.1:8000/login/attempt', data=uid_data)
#
# print(senduid)

# authenticate = requests.get(url='http://127.0.0.1:8000/login/attempt/' + str(uid_data))
#
# print(authenticate)

# -------------------------------Terminal command in python script----------------------------------------------
# os.system("python3 /home/weijin/PycharmProjects/testhowdy/cli/analyseface.py &")
# print("Hello")
#
# # -------------------------------Terminate python script from another script via subprocess----------------------------------------------
# import subprocess as sp
# #
# extProc = sp.Popen(['python3','analyseface.py']) # runs myPyScript.py
# status = sp.Popen.poll(extProc)
#
# print("In the midle of doing other things...")
#
# #
# # status should be 'None'
# print(status)
#
# def stop():
#     sp.Popen.terminate(extProc) # closes the process
#     status = sp.Popen.poll(extProc)


# -------------------------------Terminate python script from another script via pkill----------------------------------------------
#
# import os
# os.system('pkill -9 -f analyseface.py')

os.system('nohup python3 analyseface.py')





