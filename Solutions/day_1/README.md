# AWS Assignment Day-1

### Task 1

> Create a vpc through wizard, having one public subnet and one private subnet.

### Task 2

> Create two instances within the vpc that you created in task 1, windows instance in public subnet and linux instance in private subnet. Check if linux is pingable from windows.
For vice versa, make linux instance public & windows instance private then ping it too windows instance from Linux instance. 

PS: Create a Bastion Host in Public Subnet

### Task 3

> Delete all the instances and now make those two instances that you created in previous task using aws-cli.



**USING AWS-CLI**


1. Creating VPC

```
aws ec2 create-vpc --cidr-block 10.0.0.0/26
```

![Screenshots](Screenshots/1.png)


2. Setting Tags for VPC

```
aws ec2 create-tags --resources vpc-0186ea191f2032447 --tags Key=Name,Value=TEST_VPC_CLI
```

![Screenshots](Screenshots/2.png)

### Output 

![Screenshots](Screenshots/3.png)
