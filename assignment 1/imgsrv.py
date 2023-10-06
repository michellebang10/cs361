import time

while True:
    time.sleep(3)
    f = open("image-service.txt", "r")
    num = f.read()
    f.close()
    if num == type(number):
        new_num = num % 5
        f = open("image-service.txt", "w")
        f.write("./images/" + str(new_num) + ".JPG")
        f.close()
