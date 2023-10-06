import time

while True:
    print("Type 1 to generate new image or 2 to exit")
    userInput = input()
    if userInput == 1:
        f = open("prng-service.txt", "r+")
        f.write("run")
        time.sleep(5)
        num = f.read()
        fi = open("image-service.txt", "r+")
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
