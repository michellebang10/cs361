import time
import os

#title: imgsrv.py

while True:
    time.sleep(1)
    f = open("assignment 1/image-service.txt", "r+")
    num = f.read()
    if num.isnumeric():
        f.seek(0)
        f.truncate(0)
        f = open("assignment 1/image-service.txt", "w")
        new_num = (int(num) % 5) + 1
        f.write("assignment 1/images/" + str(new_num) + ".JPG")
    f.close()
