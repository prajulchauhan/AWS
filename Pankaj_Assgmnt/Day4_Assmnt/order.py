import boto3
import os
import sys

result = ""

client = boto3.client('ec2',region_name='us-east-2') #Add your region

#instanceId = (os.system('aws ec2 describe-instances  --filter Name=tag:Name,Values=nginx  --query "Reservations[*].Instances[*].InstanceId"  --output text'))
instanceId = ["i-01f7ed41dfa2f6634","i-04a51b1731ea7557c","i-05476325b25c40adb"]
length = len(instanceId)
length -= length
def instanceStart():
    print("starting Instance ...")
    
    try:
      
        for i in range(len(instanceId)):
            print(instanceId[i])
            responses = client.start_instances(
            InstanceIds=[
                instanceId[i]
            ]
            )
         
    except:
        print("Sorry :-( Starting Instance Failed !!")

def instanceStop():

    print("stopping Instance ...")
    try:        
        for i in range(len(instanceId)):
            print(instanceId[length-i])
            responses = client.stop_instances(
            InstanceIds=[
                instanceId[length-i]
            ]
            )
    except:
        print("Sorry :-( Stopping Instance Failed !!")

def changeInstanceState():

    if ((sys.argv[1]) == 'start'):
        instanceStart()
    elif ((sys.argv[1]) == 'stop'):
        instanceStop()
    else:
        print("Usage:aws.py start|stop")


changeInstanceState()
