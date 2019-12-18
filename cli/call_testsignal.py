import os

# os.system("ps -ef | grep testsignal.py | awk '{print $2}' | head -1 ")
# os.system("ps -ef | grep analyseface.py | head -1| awk '{print $2}' | xargs kill -USR1 ")
os.system("ps -ef | grep analyseface.py | head -1| awk '{print $2}' | xargs kill -USR2 ")

print("My job is done now.")