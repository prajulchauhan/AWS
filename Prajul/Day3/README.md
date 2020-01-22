# AWS Assignment Day-3

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/AWS_Simple_Icons_AWS_Cloud.svg/100px-AWS_Simple_Icons_AWS_Cloud.svg.png)](https://nodesource.com/products/nsolid)


## Task 1
> Create a linux t2.micro ec2 instance. After logging into this instance move /etc/sudoers file with /etc/sudoers.bkp 




	Launch a t2.micro instance and connect to it on starting. Move sudoers to .bkp and exit the instance. Again try to connect the instance and you will see, you can connect to it.




![image](image/1.png)




![image](image/2.png)




![image](image/3.png)



> Now try to login, If can't - resolve this issue


## Task 2

> create an ansible role before pushing the same to your public github repository.




	Role is created & pushed to repo. 



![image](mage/4.png)



![image](image/5.png)



> This Role will simply host an nginx webpage saying
  - "Hi i am ninja and my name is {yourname}" 



![image](image/8.png)



![image](image/6.png)



> Execute this role in user data script while launching another instance




![image](image/7.png)



![image](image/9.png)



> Your website should be up & running after the system boots up
> tag this instance as `ninja:yourname`




![image](image/6.png)



### Task 3
> write a jobDsl to start stop this instance through jenkins  



![image](image/10.png)



![image](image/13.png)



![image](image/14.png)



![image](image/11.png)



![image](image/12.png)



![image](image/15.png)


#  NOTE!
  - Make Documentation
  - Don't commit and push your AWS Keys on any public repository
  
   

