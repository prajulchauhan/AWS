# AWS Assignment Day-1 Solution

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/AWS_Simple_Icons_AWS_Cloud.svg/100px-AWS_Simple_Icons_AWS_Cloud.svg.png)](https://nodesource.com/products/nsolid)


## Task 1

> Create a vpc through wizard, having one public subnet and one private subnet.




	We have to create a vpc using wizard. Choose the second option in which it will automatically create a public and private subnet for us.




	
![image](image/1.png)





![image](image/2.png)





![image](image/3.png)





## Task 2
> Create two instances within the vpc that you created in task 1, windows instance in public subnet and linux instance in private subnet. check if linux is pingable from windows and vice versa.





	As for this task, let's create two instances now. Make sure to place the windows instance in public subnet & linux instance in private. In the pictures below, you'll see how I set them up.





![image](image/4.png)




![image](image/5.png)




![image](image/6.png)
	


![image](image/7.png)




![image](image/8.png)




![image](image/9.png)




![image](image/10.png)




![image](image/11.png)




![image](image/12.png)





	Now for vice-versa, create a bastian host. Bastian host is used to access instances in our private subnet. 

	First of all, change your instances, have your linux instance in public subnet & windows instance in private subnet.

	Now, create a bastian host in public subnet and connect to it using RDP.




![image](image/13.png)




![image](image/14.png)




![image](image/15.png)





	Use your bastian instance as a jump server to connect to private instance through RDP again and disable private insatnces firewall.



	Try ping it again now.




![image](image/16.png)




![image](image/17.png) 




### Task 3
> Delete all the instances and now make those two instances that you created in previous task using aws-cli.



![image](image/18.png)



![image](image/19.png)



![image](image/20.png)



![image](image/21.png)



![image](image/22.png)



![image](image/23.png)



![image](image/24.png)



![image](image/25.png)



![image](image/26.png)



#  NOTE!
  - Make Documentation and push to the repo

