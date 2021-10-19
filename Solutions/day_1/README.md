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


9. Create Internet Gateway

```
aws ec2 create-internet-gateway
```

![Screenshots](Screenshots/14.png)


10. Tagging Internet Gateway

```
aws ec2 create-tags --resources igw-02a74163f618830be --tags Key=Name,Value=CLI-IG
```

![Screenshots](Screenshots/15.png)

#### Output

![Screenshots](Screenshots/16.png)


11. Attach Internet Gateway

```
aws ec2 attach-internet-gateway --internet-gateway-id igw-02a74163f618830be --vpc-id vpc-0186ea191f2032447
```

![Screenshots](Screenshots/17.png)

#### Output

![Screenshots](Screenshots/18.png)


12. Allocate Elastic IP

```
aws ec2 allocate-address --domain vpc
```

![Screenshots](Screenshots/19.png)

#### Output

![Screenshots](Screenshots/20.png)


13. Tagging Elastic IP

```
aws ec2 create-tags --resources eipalloc-0b51fe4a278417bb0 --tags Key=Name,Value=CLI-EIP
```

![Screenshots](Screenshots/21.png)

#### Output

![Screenshots](Screenshots/22.png)


14. Create a Nat-Gateway and place it in the Public Subnet

```
aws ec2 create-nat-gateway --subnet-id subnet-0609525a055503ff4 --allocation-id eipalloc-0b51fe4a278417bb0
```

![Screenshots](Screenshots/23.png)

#### Output

![Screenshots](Screenshots/24.png)


15. Tagging Nat-Gateway

```
aws ec2 create-tags --resources nat-0a5c6e4f8760a16e7 --tags Key=Name,Value=CLI-NAT
```

![Screenshots](Screenshots/25.png)

#### Output

![Screenshots](Screenshots/26.png)


16. Create Route Table 1 for Public Subnet

```
aws ec2 create-route-table --vpc-id vpc-0186ea191f2032447
```

![Screenshots](Screenshots/27.png)


17. Tagging Public RT

```
aws ec2 create-tags --resources rtb-0584a3ac1c717b616 --tags Key=Name,Value=CLI-PUBLIC_RT
```

![Screenshots](Screenshots/28.png)

#### Output

![Screenshots](Screenshots/29.png)


18. 








