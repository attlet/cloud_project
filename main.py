import boto3


def listInstance():
    print("list instance")


def availableZone():
    print("available zone")


def startInstance():
    print("start instance")


def availableRegion():
    print("available Region")


def stopInstance():
    print("stop instance")


def createInstance():
    print("create instance")


def rebootInstance():
    print("reboot instance")


def listImage():
    print("list image")


def main():
    while True:
        print("\n")
        print("------------------------------------------------------------\n")
        print("           Amazon AWS Control Panel using SDK               \n")
        print("------------------------------------------------------------\n")
        print("  1. list instance                2. available zones        \n")
        print("  3. start instance               4. available regions      \n")
        print("  5. stop instance                6. create instance        \n")
        print("  7. reboot instance              8. list images            \n")
        print("                                 99. quit                   \n")
        print("------------------------------------------------------------\n")
        print("Enter an integer: ")

        number = input()
        if int(number) != number:
            print("concentration!")
            break

        if number == 1:
            listInstance()
        elif number == 2:
            availableZone()
        elif number == 3:
            startInstance()
        elif number == 4:
            availableRegion()
        elif number == 5:
            stopInstance()
        elif number == 6:
            createInstance()
        elif number == 7:
            rebootInstance()
        elif number == 8:
            listImage()
        elif number == 99:
            print("bye!\n")
            return
        else:
            print("concentration!")
            
        
  

if __name__ == "__main__":
    main()
