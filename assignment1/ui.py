import time

#title: ui.py

while True:
    print("Type 1 to generate new image or 2 to exit")
    userInput = int(input("Input: "))
    if userInput == 1:
        f = open("prng-service.txt", "w")
        f.write("run")
        time.sleep(2)
        f.close()
        time.sleep(5)
        f = open("prng-service.txt", "r")
        num = f.read()
        fi = open("image-service.txt", "w")
        fi.write(num)
        fi.close()
        time.sleep(5)
        fi = open("image-service.txt", "r")
        output = fi.read()
        print(output)
    elif userInput == 2:
        break
    else:
        print("Unknown option")

    f.close()
    fi.close()
