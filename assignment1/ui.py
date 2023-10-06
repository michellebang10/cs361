import time

#title: ui.py

while True:
    print("Type 1 to generate new image or 2 to exit")
    userInput = int(input("Input: "))
    if userInput == 1:
        f = open("prng-service.txt", "r+")
        f.seek(0)
        f.truncate(0)
        f.write("run")
        time.sleep(5)
        num = f.read()
        fi = open("image-service.txt", "r+")
        fi.write(num)
        time.sleep(5)
        output = fi.read()
        print(output)
    elif userInput == 2:
        break
    else:
        print("Unknown option")
    f.close()
    fi.close()
