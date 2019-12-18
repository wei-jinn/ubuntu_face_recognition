import signal
import os
import time

signum = "0"
pid = os.getpid()

def receive_signal(signum, stack):
    print ('Received:', signum)
    print("I got your signal, let me sleep awhile")
    time.sleep(10)
    print("Let's go back to work")
    print("My pid is ", pid)

signal.signal(signal.SIGUSR1, receive_signal)
# ps -ef | grep testsignal.py | awk '{print $2}' | xargs kill -USR1
signal.signal(signal.SIGUSR2, receive_signal)

print('My PID is:', os.getpid())

while True:
    print('Waiting...')
    time.sleep(3)
    print('Received:'+ signum)
