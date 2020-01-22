# AWS Assignment Day-8
 
[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/AWS_Simple_Icons_AWS_Cloud.svg/100px-AWS_Simple_Icons_AWS_Cloud.svg.png)](https://nodesource.com/products/nsolid)


### Task 1
> Create an infrastructure that would scale as per load:

 * Go to Launch Configuration -> ``` Create Launch Configuration ```

 ![](images/lc.png)

    add configuration of instances you need to have
 
 ![](images/confLC.png)

 
 * Now after Creating LC create a auto scaling group

 ![](images/autoscaling.png)
 ( Creating make sure to check each and every steps and configuration [Although You can edit them later too])

 ![](images/sca.png)
 (you have created a acalable group)

 ![](images/setcal.png)

 * policy of My scale group
 ![](images/scaepolicy.png)

> Create cloudwatch alarms for scaling up and scaling down along with sns topic to notify you during any scaling operation
  
   * After Creating these configuration Create alarm "But Before Alarm try to add Sns service active in any email account"
  
  - scale up if av. cpu threashold > 70

  ![](images/70.png)
  
  - scale down if av. cpu threashold < 50
  ![](images/thresbelow.png)
  
* IN SNS Service create Sns

![](images/sns.png)

* Approve the notification service from your email account

![](images/cofrim.png)

``` Below steps are if you did not set the alarm from scale group policies ```

* Create Matrics for the scale group
![](images/createmetric.png)

* Set Metrics
![](images/setmetric.png)

* Set threshold
![](images/70alarm.png)
(you must have created this from scale group while adding policies. If not You can from Cloudwatch dashboard)

* set email topic
![](images/settopic.png)
  
* Select scale group you created earlier
![](images/seelctsc.png)

#### After These Steps You must have created below services

* Launch Configuration
* Auto Scaling Group
* Alarm {CloudWatch Dashboard}
* SNS Service

#### Add Fake traffic to your instance

* For this You will have to install Apache Bench in server instance to genrate fake load {via ssh}

https://www.tutorialspoint.com/apache_bench/apache_bench_environment_setup.htm

* After installing you can hit this command from cli 

``` ab -n 1000000 -c 10 https://www.apache.org/ ```


![](images/apache.png)

* Now you will get a email when cpu utilization become > 70
![](images/email.png)

* You wil reach this location 
![](images/link.png)

* Your cloudwatch dashboard
![](images/alarmdahs.png)

* The graph utilization you can see from 
![](images/graph.png)


* Now you will see the new instances in ec2 instance panel and you can also see them in your auto scaling group
![](images/in.png)

* If the Cpu utilization goes down the instances will gets terminate automatilly
![](images/one.png)

* and finally you will reach to The desired count of instances which in my ase was 1
![](images/desired.png)

  - `First do it via console and then via aws cli`


#  NOTE!
  - Make sure you explore other matrices as well for scaling like memory, network etc..
  - Make Documentation

