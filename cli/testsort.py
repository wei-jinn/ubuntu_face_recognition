# from datetime import datetime
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
word = '184471-Chiew_Jia_Jing'

# Substring is searched in 'eks for geeks'
position = word.find('-', 0)
length = len(word)
print(position)
print(length)
matric = word[0:position]
name = word[position+1:length]
fullname = name.replace("_", " ")

print(matric)
print(fullname)
