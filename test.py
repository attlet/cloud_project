import boto3

access_key = ""
secret_key = ""
region = "ap-northeast-2"




def listInstance(ec2):
    
    print("Listing instance....\n")
    ec2_list = ec2.instances.all()
    
    for instance in ec2_list:
        print("[id]  " + instance.id + "  [AMI]  " + instance.image_id + "  [type]  " + instance.instance_type + "  [state]  " + instance.state["Name"] + "  [mornitoring state]  " + instance.monitoring['State'] + '\n')
        
    

def availableZone(ec2):
    print("available zone")


def startInstance(ec2):
    print("start instance")
    Input_id = input("Enter instance id: ")
    print("Starting ...   " + Input_id)
    instance = ec2.Instance(Input_id)
    
    if instance.state['Name'] == 'stopped':
        instance.start()
    

    print("Successfully started instance " + Input_id)
    


def availableRegion(ec2):
    print("available Region")


def stopInstance(ec2):
    print("stop instance")


def createInstance(ec2):
    Input_id = input("Enter ami id: ")
    instances = ec2.create_instances(
        ImageId=Input_id,
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="master"
    )
    
    print("Successfully started EC2 instance " + instances[0].instance_id + " based on AMI " + Input_id)


def rebootInstance(ec2):
    print("reboot instance")


def listImage(ec2):
    print("Listing image...\n")
    image_list = ec2.images.filter(Owners=['self'])
    
    for image in image_list:
        print("[ImageID]  " + image.id + "  [Name]  " + image.name + "  [Owner]  " + image.owner_id)
        
    


def main():

    while True:
        ec2 = boto3.resource('ec2', aws_access_key_id=access_key,
                     aws_secret_access_key=secret_key, region_name=region)
        
        print("\n")
        print("------------------------------------------------------------\n")
        print("           Amazon AWS Control Panel using SDK               \n")
        print("------------------------------------------------------------\n")
        print("  1. list instance                2. available zones        \n")
        print("  3. start instance               4. available regions      \n")
        print("  5. stop instance                6. create instance        \n")
        print("  7. reboot instance              8. list images            \n")
        print("                                 99. quit                   \n")
        print("------------------------------------------------------------")

        try:
            number = int(input("Enter an integer: "))
        except ValueError:
            print("concentrate!")
            break

        if number == 1:
            listInstance(ec2)
        elif number == 2:
            availableZone(ec2)
        elif number == 3:
            startInstance(ec2)
        elif number == 4:
            availableRegion(ec2)
        elif number == 5:
            stopInstance(ec2)
        elif number == 6:
            createInstance(ec2)
        elif number == 7:
            rebootInstance(ec2)
        elif number == 8:
            listImage(ec2)
        elif number == 99:
            print("bye!\n")
            return
        else:
            print("concentration!")


if __name__ == "__main__":
    main()
