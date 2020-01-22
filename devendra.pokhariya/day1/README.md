# AWS Assignment Day-1

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/AWS_Simple_Icons_AWS_Cloud.svg/100px-AWS_Simple_Icons_AWS_Cloud.svg.png)](https://nodesource.com/products/nsolid)


### Task 1
> Create a vpc through wizard, having one public subnet and one private subnet.
 
 * You can create a VPC from VPC dashboard you will see the "LAUNCH VPC WIZARD" button at the top of the page
    Once You are in you will get these option
 ![image](images/optionvpc.png)
    
    Select the second as per task then select the network Id and subnet Cidr from this page  
 ![image](images/Subnetnvp.png)

 * After selecting the proper subnet and netwok id you will get (This step will atuomatically allocate a route table and internet gateway and NAT gateeway by default)

 ![image](images/wizardvpc.png)

### Task 2
> Create two instances within the vpc that you created in task 1, windows instance in public subnet and linux instance in private subnet. check if linux is pingable from windows and vice versa.


 * Create Two instance from Ec2 dashoard one linux and select VPC which you have created from Wizard also Make sure you choose public subnet for windows (i.e, public Instance) and do not forge to make the security group. 

  ![image](images/intance.png)

 * Finally You will have 2 Instances with different subnet (Public and Private)

  ![image](images/inst.png)

 * Now One Important thing you will have to do before doing ping it to update your security group rules as below

    ![image](images/winSG.png)
    (this is your windows inbound security group rules)

    Linux Private Security Group 

    ![image](images/linuxSG.png)


 * Connect to the window through RDP client software

 ![image](images/connectwindo.png)
    (You will get a public ip I a showing you private Ip here ) 😃

* Now once you are in RDP You will get a windows OS environment and display

 ![image](images/succcessfullRdp.png)



* Now open cmd in windows instance and ping your Linux Instance.

![image](images/pinglinux.png)

    Success !! 🤘
 
 * Next for vise-versa You need to make Linux instance public and windows private ( Create New Instances

 * Follow same procedure and if you want to create new VPC create or add new instances in previously added VPC in public and Private subnet Linux and windoews simultenously. 

 * One major thing you will have to achive before you can ping your private windows is by  wnabling inbound rule inside your new private windows server 
 * which can be done by creating a new windows instance in same VPC (In need to access rdp to your private windows instance) 
 * Create new Windows instace in same VPC allowing rdp access from anywhere then access this new windows Instace from connect and using your RDP credentials

 * After successful connection you will be inside you public windows instance (call it Jump server)

 * Inside you Jump windows server open rdp and use your private windows credentials

 * In that enable the Ipv4 rule 
 ![image](images/allowipv4impc.png)
 
  * check the video for more info
   
    ```  https://www.youtube.com/watch?v=3XxQtZ2j4Mo ```

 * Once you have achived this correctly you will be able to ping the windows server

  ![image](images/pingwindowprivate.png)

     P.s. I am using putty to ssh to my public instance

### Task 3
> Delete all the instances and now make those two instances that you created in previous task using aws-cli.

  * After deleting you have to install aws cli in your system
  
  * configure aws on your system {aws configure}

  ``` 
      aws ec2 run-instances --image-id {os image id}  --count 2 --instance-type t2.micro --associate-public-ip-address --key-name {Key pair name} --security-group-ids {Security gp name} --subnet-id {Subnet id} --region us-east-2

  ```
  (Change the names in braces {} )

   ![](images/aws-cli.png)

   * Now add tag name

      ```
         aws ec2 create-tags --resources {instance id} --tags Key=Name,Value=Dev_From_CLi

      ```

      ![](images/weinst.png)

#  NOTE!
  - Make Documentation and push to the repo

