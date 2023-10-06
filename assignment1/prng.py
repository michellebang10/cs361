import random
import sys
import time
import os


#title: prng.py

while True:
    time.sleep(1)
    f = open("prng-service.txt", "r+")
    text = f.read()
    if text == "run":
        time.sleep(3)
        num = random.randint(1, sys.maxsize)
        f.seek(0)
        f.truncate(0)
        f.write(str(num))
    f.close()


