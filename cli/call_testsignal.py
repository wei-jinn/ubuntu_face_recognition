import os

# to see the script.py running process id(print $2)/ username(print $1), "head -1" means only return first pid
# os.system("ps -ef | grep testsignal.py | awk '{print $2}' | head -1 ")

# to kill python script via the script name
# os.system("pkill -9 -f script.py")

# os.system("ps -ef | grep analyseface.py | head -1| awk '{print $2}' | xargs kill -USR1 ")
os.system("ps -ef | grep analyseface.py | head -1| awk '{print $2}' | xargs kill -USR2 ")

print("My job is done now.")