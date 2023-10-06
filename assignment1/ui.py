import time
import os

#title: ui.py

while True:
    print("Type 1 to generate new image or 2 to exit")
    userInput = int(input("Input: "))
    if userInput == 1:
        f = open("assignment 1/prng-service.txt", "r+")
        #if os.path.getsize("assignment 1/prng-service.txt") != 0:
        f.seek(0)
        f.truncate(0)
        f.write("run")
        time.sleep(5)
        num = f.read()
        fi = open("assignment 1/image-service.txt", "r+")
        fi.write(num)
        time.sleep(5)
        output = fi.read()
        print(output)
        f.close()
        fi.close()
    elif userInput == 2:
        break
    else:
        print("Unknown option")
