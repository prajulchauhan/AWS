Task 1

Host a static website using s3 as follows:

Buy a domain from Freenom as yourname.opstree.com
 example: yashvinderopstree.com (Don't worry it's free)

```
Open your freenom account and check availibilty of your domain name
Then select domain of your choice (.tk, .ml etc)
```
![image](images/1.png)

```
Now register your domain
```
![image](images/2.png)

Migrate this domain to Route53
```
Now navigate to AWS Route53 service and select Create hosted zone in DNS management fill details accordingly
```
![image](images/3.png)

![image](images/4.png)

![image](images/5.png)

![image](images/6.png)

```
Now manage the nameservers in freenom accordingly
```
![image](images/7.png)

Host a static website using s3 bucket

```
Now create a S3 bucket same name as your domain name
```
![image](images/8.png)

![image](images/9.png)

```
enable it for static hosting
```
![image](images/10.png)

```
Attach your bucket in Route53
```

![image](images/11.png)

```
Now check in few minutes your website will be hosted
```

![image](images/12.png)

link for website

http://pankajopstree.ml/

NOTE!

Make Documentation