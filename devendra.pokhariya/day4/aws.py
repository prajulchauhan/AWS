import boto3
import os
import sys

client = boto3.client('ec2',region_name='us-east-2') #Add your region
instanceId =[]
tagName = ['1','2', '3'] # Boot Order

length =len(tagName)
for i in range(length):
    instanceId.append(os.popen('aws ec2 describe-instances  --filter Name=tag:Boot-order,Values='+tagName[i]+' --query "Reservations[*].Instances[*].InstanceId"  --output text').read())

length = len(instanceId)
for i in range(length):
	instanceId[i] = instanceId[i].replace("\n", "")


def instanceStart():
    print("starting Instance From 3...1")
    
    try:
        for i in range(length):
            print(instanceId[i])
            responses = client.start_instances(
            InstanceIds=[
                instanceId[i]
            ]
            )
         
    except:
        print("Sorry :-( Starting Instance Failed !!")

def instanceStop():

    print("stopping Instance From Boot Order 1...3")
    try:        
        for i in range(length):
            print(instanceId[(length -1 ) -i])
            responses = client.stop_instances(
            InstanceIds=[
                instanceId[(length -1) -i]
            ]
            )
    except:
        print("Sorry :-( Stopping Instance Failed !!")

def changeInstanceState():

    if len(sys.argv) > 1:
        if ((sys.argv[1]) == 'start'):
            instanceStart()
        elif ((sys.argv[1]) == 'stop'):
            instanceStop()
        else:
            print("Usage:aws.py start|stop")
    else:
        print("Usage:aws.py start|stop")


changeInstanceState()