import time
import os

#title: imgsrv.py

"""
Note: 
file 0: pilot pochacco
file 1: winking pochacco
file 2: musician pochacco
file 3: astronaut pochacco
file 4: sleeping pochacco
"""

while True:
    time.sleep(5)
    f = open("image-service.txt", "r+")
    num = f.read()
    path = "/Users/michellebang/cs361/assignment1/images"
    files = os.listdir(path)
    if num.isnumeric():
        new_num = (int(num) % len(files))
        f.seek(0)
        f.truncate(0)
        f.write(files[new_num])
    f.close()
