import random
import sys
import time

while True:
    time.sleep(3)
    f = open("prng-service.txt", "r")
    text = f.read()
    f.close()
    if text == "run":
        num = random.randint(1, sys.maxsize)
        f = open("prng-service.txt", "w")
        f.write(num)
        f.close()


