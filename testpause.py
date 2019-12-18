import os
import sys
import time


# ________________________Run script in background_______________________________
def increment():
    number = 0
    while True:
        number +=1
        print(number)


def stop():
    sys.exit(0)

