import boto3
import time

access_key = ""
secret_key = ""
region = "ap-northeast-2"




def listInstance(ec2):
    
    print("Listing instance....\n")
    ec2_list = ec2.instances.all()
    
    for instance in ec2_list:
        print("[id]  " + instance.id + "  [AMI]  " + instance.image_id + "  [type]  " + instance.instance_type + "  [state]  " + instance.state["Name"] + "  [mornitoring state]  " + instance.monitoring['State'] + '\n')
        
    

def availableZone(ec2):
    print("Available zone... \n")
    client = boto3.client('ec2',aws_access_key_id=access_key,
                     aws_secret_access_key=secret_key, region_name=region)
    
    response = client.describe_availability_zones()
    instances = response['AvailabilityZones']
    
    cnt = 0
    for instance in instances:
        print("[id]  " + instance['ZoneId'] + "  [region]  " + instance['RegionName'] + "  [zone]  " + instance['ZoneName'])
        cnt += 1
    
    print("You have access to " + str(cnt) + " Zones")


def startInstance(ec2):
    print("start instance")
    Input_id = input("Enter instance id: ")
    print("Starting ...   " + Input_id)
    instance = ec2.Instance(Input_id)
    
    if instance.state['Name'] == 'stopped':
        instance.start()
        print("Successfully started instance " + Input_id)
    else :
        print("Instance aleady running")

    
def availableRegion(ec2):
    print("Available Region...\n")
    
    client = boto3.client('ec2',aws_access_key_id=access_key,
                     aws_secret_access_key=secret_key, region_name=region)
    
    response = client.describe_regions()
    instances = response['Regions']
    
  
    for instance in instances:
        print("[region]  " + instance['RegionName'] + "  [endpoint]  " + instance['Endpoint'])
        

def stopInstance(ec2):
    Input_id = input("Enter instance id : ")
    instance = ec2.Instance(Input_id)
    
    if instance.state['Name'] == 'running':
        instance.stop() 
        print("Successfully stop instance " + Input_id)
    else:
        print("Instance aleady stopped")
   


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
    Input_id = input("Enter ami id: ")
    instance = ec2.Instance(Input_id)
    print("Rebooting..." + Input_id + "\n")
    
    if instance.state['Name'] == "running":
        instance.reboot()
        print("Successfully rebooted instance " + Input_id)
    else:
        print("Cannot reboot : stopped instance\n")
        


def listImage(ec2):
    print("Listing image...\n")
    image_list = ec2.images.filter(Owners=['self'])
    
    for image in image_list:
        print("[ImageID]  " + image.id + "  [Name]  " + image.name + "  [Owner]  " + image.owner_id)
        
def Condor_status(ec2):
    print("Condor_status\n")
    client = boto3.client('ssm',aws_access_key_id=access_key,
                     aws_secret_access_key=secret_key, region_name=region)
      
    response = client.send_command(
        InstanceIds=['i-00560e4f1c655604f'],
        DocumentName='AWS-RunShellScript',
        Parameters={'commands': ['condor_status']}
    )
    command_id = response['Command']['CommandId']
    time.sleep(2)
    output = client.get_command_invocation(
      CommandId=command_id,
      InstanceId='i-00560e4f1c655604f',
    )
    
    ret = output['StandardOutputContent']
    print(ret)
    
    

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
        print("  9. condor_status                                          \n")
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
        elif number == 9:
            Condor_status(ec2)
        elif number == 99:
            print("bye!\n")
            return
        else:
            print("concentration!")


if __name__ == "__main__":
    main()
