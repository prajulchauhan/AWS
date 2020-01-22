# AWS Assignment Day-7
 
[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/AWS_Simple_Icons_AWS_Cloud.svg/100px-AWS_Simple_Icons_AWS_Cloud.svg.png)](https://nodesource.com/products/nsolid)


### Task 1
> Rajat is the devops guy in 'abc' organization 

and he is responsible for creating 't2.micro' and all the 'm' family of instances as per requirement but he can't terminate 'm' family of instances but that's not the case with t2.micro.

#### create a IAM Group Name it 
  ``` EC2MfamilyRole ```

 Tejasvi Rana has got root access to the account but he isn't a technical guy.
 
  He is always suspicious about Rajat's actions in company's aws account. 
  
  Luckily Tejasvi has got a friend, Priyanka jugran, she is amazon certified and knows everything about aws. Tejasvi wants Priyanka to cross check rajat's IAM permissions.
 In order to do that, he gave priyanaka full access. 

 #### Create new IAM group with admin access name it

  ``` AdminAcess ```  
 
 
 Now priyanka needs s3 storage for one of her friend, priyanka sharama to run athena queries for data analysis,they don't want to pay for that from their own aws account.

  Jugran has created a bucket with name 'abc-data' with a policy that sharma will only be able to access this bucket from a particular ec2 instance that she created & provided the user details to sharma. 

 #### from Jugran account create IAM ROLE [attach that role to instance which will access s3 bucket]

  ``` EC2toS3Acess ```
 #### You will create a IAM User Priyanka Sharma  and a Group 
 
  ``` Ec2Access ```

 Rajat referenced his friends kavit and vishwas to his organization and now all of then share the same permission level.

 #### Add new user in previouslt build IAM Group {EC2MfamilyRole} 

  ``` add kavit vishwas in this EC2MfamilyRole group```

  Kushgra is also one of the team memebers from operations team but recently he has got a task to create and run lambda function that is going to access rds database. 
  
 #### Add new group with Lambda and RDS access

  ``` LambdaRds```
  
  - How many IAM groups gets created 
  
  ``` From My perspective It would create 4 Group```
  * Group 1st ==> EC2MfamilyRole {Rajat | Kavit | Vishwas}
  * Group 2nd ==> AdminAcess {Priyanka Jugran}
  * Group 3rd ==> Ec2Access {Priyanka Sharma}
  * Group 4th ==> LambdaRds {Kushgra}
  
  - One IAM Role

  * Role 1 ==>  EC2toS3Acess { Ec2 To S3 Access }

  - How many IAM users gets created 

  ``` And If we are moving forward, then we can make these IAM users too. Total of 6 User  ```
  * IAMUSER 1st ==> RAJAT
  * IAMUSER 2nd ==> Kavit
  * IAMUSER 3rd ==> Vishwas
  * IAMUSER 4th ==> Priyanka Jugran
  * IAMUSER 5th ==> Priyanka Sharma
  * IAMUSER 6th ==> Kushgara


  - Permissions associated with them

  ``` Policies Associated  There will Be maximum of 5 Policies```
  * Policy One ==> EC2 Instance {EC2MfamilyRole}
  * Policy Two ==> ADMINACCESS {AdminAcess}
  * Policy Three ==> S3 Access {EC2toS3Acess}
  * Policy Four ==> Lambda Access & RDS {LambdaRds}
  * Policy Five ==> EC2 Instance Access {Ec2Access}


#  NOTE!
  - Make Documentation

