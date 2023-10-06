import random
import sys
import time


#title: prng.py

while True:
    time.sleep(5)
    f = open("prng-service.txt", "r+")
    text = f.read()
    if text == "run":
        num = random.randint(1, sys.maxsize)
        f.seek(0)
        f.truncate(0)
        f.write(str(num))
    f.close()


