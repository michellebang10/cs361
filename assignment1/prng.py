import random
import sys
import time
import os


#title: prng.py

while True:
    time.sleep(1)
    f = open("assignment 1/prng-service.txt", "r+")
    text = f.read()
    if text == "run":
        #if os.path.getsize("assignment 1/prng-service.txt") != 0:
        f.seek(0)
        f.truncate(0)
        f = open("assignment 1/prng-service.txt", "w")
        num = random.randint(1, sys.maxsize)
        f.write(str(num))
    f.close()


