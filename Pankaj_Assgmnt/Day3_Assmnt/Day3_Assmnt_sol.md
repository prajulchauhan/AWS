AWS Assignment Day-3


Task 1

Create a linux t2.micro ec2 instance. After logging into this instance move /etc/sudoers file with /etc/sudoers.bkp

```
To launch an EC2 instance

1. Open the Amazon EC2 console

2. From the dashboard, choose Launch Instance.

3. On the first page of the wizard, choose the AMI that you want to use( Linux ). On the Choose an Instance Type page, you can select the hardware configuration and size of the instance to launch

5. Go through configure Instance Details page and go through the next pages of the wizard until you get to the Add Tags page

6. On the Add Tags page, you can tag your instance with a Name tag; for example Name=LinuxMachine. This helps you to identify your instance in the Amazon EC2 console after you've launched it

7. Now complete Configure Security group and other steps and launch.

```

![image](images/1.png)

![image](images/2.png)

![image](images/3.png)

![image](images/4.png)

```
Now connect to your instance using ssh private key file and move /etc/sudoers file with /etc/sudoers.bkp
```

![image](images/5.png)

![image](images/6.png)

Now try to login, If can't - resolve this issue

```
Still able to login in in instance
```

![image](images/7.png)

Task 2

create an ansible role before pushing the same to your public github repository.

This Role will simply host an nginx webpage saying

"Hi i am ninja and my name is {yourname}"

![image](images/8.png)

![image](images/9.png)

Execute this role in user data script while launching another instance

![image](images/12.png)

```
When you launch an instance in Amazon EC2, you have the option of passing user data to the instance that can be used to perform common automated configuration tasks and even run scripts after the instance starts

Here we will write a script to install python, git and ansible.
then clone our public git repo and execute role for nginx by using cloned repo
```

![image](images/13.png)

![image](images/14.png)

![image](images/15.png)

Your website should be up & running after the system boots up

![image](images/11.png)

tag this instance as ninja:yourname

![image](images/10.png)

Task 3

write a jobDsl to start stop this instance through jenkins

```
Create Jenkins Job to start and Stop Ec2 instance

Create a parameterized build to pass the Ec2 Instance id and Ec2 State name in Start or Stop

```

![image](images/16.png)

![image](images/17.png)

```
Create Write Shell script in Build Step
```

![image](images/18.png)

![image](images/19.png)

![image](images/20.png)

![image](images/21.png)

![image](images/22.png)

![image](images/23.png)

![image](images/24.png)

NOTE!

Make Documentation
Don't commit and push your AWS Keys on any public repository