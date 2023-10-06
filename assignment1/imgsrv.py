import time
import os

#title: imgsrv.py

while True:
    time.sleep(1)
    f = open("image-service.txt", "r+")
    num = f.read()
    path = "/Users/michellebang/cs361/assignment1/images"
    files = os.listdir(path)
    if num.isnumeric():
        new_num = (int(num) % len(files)) + 1
        f.seek(0)
        f.truncate(0)
        f.write(files[new_num])
    f.close()
