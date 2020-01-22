AWS Assignment Day-7


Task 1

Rajat is the devops guy in 'abc' organization and he is responsible for creating 't2.micro' and all the 'm' family of instances as per requirement but he can't terminate 'm' family of instances but that's not the case with t2.micro. Tejasvi Rana has got root access to the account but he isn't a technical guy. He is always suspicious about Rajat's actions in company's aws account. Luckily Tejasvi has got a friend, Priyanka jugran, she is amazon certified and knows everything about aws. Tejasvi wants Priyanka to cross check rajat's IAM permissions. In order to do that, he gave priyanaka full access. Now priyanka needs s3 storage for one of her friend, priyanka sharama to run athena queries for data analysis,they don't want to pay for that from their own aws account. Jugran has created a bucket with name 'abc-data' with a policy that sharma will only be able to access this bucket from a particular ec2 instance that she created & provided the user details to sharma. Rajat referenced his friends kavit and vishwas to his organization and now all of then share the same permission level.
Kushgra is also one of the team memebers from operations team but recently he has got a task to create and run lambda function that is going to access rds database.


How many IAM groups gets created

```
Total 4 groups will be Created

1. For Priyanka Jugran (FullAccess)

2. For Rajat, Kavit and Vishwas (Instance)

3. For Kushgra (LambdaRDS)

4. For Priyanka Sharma (Sharmaji)

```
How many IAM users gets created

```
Total 6 Users will be Created

1. Priyanka Jugran (will  be associated with full access group)

2. Rajat (will  be associated with Instance group)

3. Kavit (will  be associated with Instance group)

4. Vishwas (will  be associated with Instance group)

5. Kushgra (will  be associated with Lambda group)

6. Priyanka Sharma ( will  be associated with Sharmaji group)
```
Permissions associated with them

```
1. FullAccess group with Administrative Access

2. Instance group will have full access for t2.micro instances and remove terminate access for 'm' family instances

3. LambdaRDS group will have full access for Lambda Functions and read access for rds database

4. Sharmaji group will have EC2 instance access permission

5. IAM role for EC2 to access S3 bucket
```
NOTE!

Make Documentation