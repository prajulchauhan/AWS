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

#### Output 

![Screenshots](Screenshots/3.png)


3. Modifying VPC Attributes for enabling DNS Hostname

```
aws ec2 modify-vpc-attribute --vpc-id vpc-0186ea191f2032447 --enable-dns-hostname "{\"Value\":true}"
```

![Screenshots](Screenshots/4.png)

#### Output

![Screenshots](Screenshots/5.png)


4. Creating Public Subnet

```
aws ec2 create-subnet --vpc-id vpc-0186ea191f2032447 --cidr-block 10.0.0.0/27
```

![Screenshots](Screenshots/6.png)


5. Tagging Public Subnet

```
aws ec2 create-tags --resources subnet-0609525a055503ff4 --tags Key=Name,Value=CLI-Public-Subnet
```

![Screenshots](Screenshots/7.png)

#### Output

![Screenshots](Screenshots/8.png)


6. Enable auto-assign Public IP on the Public Subnet

```
aws ec2 modify-subnet-attribute --subnet-id subnet-0609525a055503ff4 --map-public-ip-on-launch
```

![Screenshots](Screenshots/9.png)

#### Output

![Screenshots](Screenshots/10.png)


7. Creating Private Subnet

```
aws ec2 create-subnet --vpc-id vpc-0186ea191f2032447 --cidr-block 10.0.0.32/27
```

![Screenshots](Screenshots/11.png)


8. Tagging Private Subnet

```
aws ec2 create-tags --resources subnet-06aa7f597b99617a3 --tags Key=Name,Value=CLI-Private-Subnet
```

![Screenshots](Screenshots/12.png)

#### Output

![Screenshots](Screenshots/13.png)


9.

