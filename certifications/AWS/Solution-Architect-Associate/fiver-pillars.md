# 1. Reliability Pillar

## 1.1 Foundation – Limit management
### 1.1.1 Key AWS Services
**AWS Trusted Advisor:** The key AWS feature that supports a way to identify what service limits currently are is AWS Trusted Advisor which provides a list of what limits it returns.
### 1.1.2 Other AWS Services
The following services and features are also important: 
* **Amazon CloudWatch:** You can set alarms to indicate when you are getting close to limits in Network IO, Provisioned IOPS, EBS and ephemeral volume capacity (through custom metrics), etc. You can also set alarms for when you are approaching maximum capacity of auto scaling groups. 
* **Amazon CloudWatch–Logs:** Metric filters can be used to search and extract patterns in a log event. Log entries are converted to numeric metrics, and alarms can be applied. 
### 1.1.3 Video Resources
* [How do I manage my AWS service limits?](https://aws.amazon.com/premiumsupport/knowledge-center/manage-service-limits/)
### 1.1.4 Documentation Resources
* [AWS Service Limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)
* [Service Limit Reports Blog Post](https://aws.amazon.com/about-aws/whats-new/2014/06/19/amazon-ec2-service-limits-report-now-available/)
* [Trusted Advisor FAQs](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/)
* [AWS Limit Monitor on AWS Answers](https://aws.amazon.com/solutions/limit-monitor/)

## 1.2 Foundation – Neworking
### 1.2.1 Key AWS Services
**Amazon Virtual Private Cloud (Amazon VPC):** The key AWS service that supports your network planning is Amazon Virtual Private Cloud (Amazon VPC), which allows you to allocate private IP address ranges to either provide non-internet-accessible resources or to extend your data center
### 1.2.2 Other AWS Services
The following services and features are also important: 
* **AWS Direct Connect:** Can be used to give a private dedicated connection to AWS for possible lower latency and consistent performance to and from AWS.
* **Amazon EC2:** If you choose to implement VPNs between your networks, this is the service on which you run VPN appliances.
* **Amazon Route 53:** A Domain Name System (DNS) service that is integrated directly with ELB and can help provide a layer of defense in the event of a DoS attack.
* **AWS Global Accelerator:** This is a network layer service that you can use to create accelerators that direct traffic to optimal endpoints over the AWS global network.
* **Elastic Load Balancing:** Provides load balancing across Availability Zones, performs Layer 7 routing, integrates with AWS WAF, and integrates with Auto Scaling to help create a self-healing infrastructure and absorb increases in traffic while releasing resources when traffic decreases.
* **AWS Shield:** Provides automatic protection against Distributed Denial of Service (DDoS) attacks at no extra cost. Additional protection within your provisioned infrastructure is available as AWS Shield Advanced and will protect Elastic Load Balancing load balancers, Amazon CloudFront distributions, and Amazon Route 53-hosted zones.
### 1.2.3 Video Resources
* [Advanced VPC Design and New Capabilities for Amazon VPC (NET305)](https://www.youtube.com/watch?v=fnxXNZdf6ew&t=1s)
* [AWS Transit Gateway and Transit VPCs (NET402)](https://www.youtube.com/watch?v=ar6sLmJ45xs)
### 1.2.4 Documentation Resources
* [Amazon Virtual Private Cloud Product Page](https://aws.amazon.com/vpc/)
* [Amazon Virtual Private Cloud Documentation](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Introduction.html)
* [Announcement on Amazon VPC allowing customers to expand their VPCs](https://aws.amazon.com/about-aws/whats-new/2017/08/amazon-virtual-private-cloud-vpc-now-allows-customers-to-expand-their-existing-vpcs/)
* [VPC Endpoint Services (AWS PrivateLink)](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/endpoint-service.html)
* [Transit Gateways](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)
* [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)
* [Amazon EC2 Instance Types Product Page](https://aws.amazon.com/ec2/instance-types/)
* [Amazon EC2 Instance Types Documentation](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)
* [AWS Marketplace for Network Infrastructure](https://aws.amazon.com/marketplace/b/2649366011/ref=gtw_navlft_node_2649366011)
* [AWS Shield Documentation](http://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html)
* [AWS Best Practices for DDoS Resiliency Whitepaper](https://d0.awsstatic.com/whitepapers/Security/DDoS_White_Paper.pdf)
* [Single Region Multi-VPC Connectivity on AWS Answers](https://aws.amazon.com/answers/networking/aws-single-region-multi-vpc-connectivity/)
• [Amazon VPC Connectivity Options Whitepaper](https://d0.awsstatic.com/whitepapers/aws-amazon-vpc-connectivity-options.pdf)


## 1.3 Application Design for High Availability
### 1.3.1 Understanding Availability Needs
### 1.3.2 Application Design for Availability
* Fault Isolation Zones
* Redundanct Components
* Microservice architecture
* Reovery Oriented Computing 
* Distributed System best practices
### 1.3.3 Operational Considerations for Availability
* Automate Deployments to Eliminate Impact
* Testing
* Monitoring and Alarming
  * Generation
  * Aggregation
  * Real-Time Processing and Alarming
  * Storage and Analytics
  * Key AWS Services
     **Amazon CloudWatch and AWS X-Ray:** 
     The key AWS service that supports monitoring is Amazon CloudWatch, which allows for easy creation of alarms that trigger scaling actions. In addition, AWS X-Ray can be integrated with your applications to provide visibility into the distributed interaction of requests with your applications
   * Other AWS Services
     The following services and features are also important: 
      * **Amazon S3:** Acts as the storage layer, and allows for lifecycle policies and data management.
      * **Amazon EMR:** Use this service to gain further insight into log and metric data.
      * **Amazon Athena:** Use this service to gain further insight into data that is in support formats.
 * Operational Readiness Reviews
 * Auditing

## 1.4 Reliability Pillar - Rerefences
* [DynamoDB: Global Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html)
* [DynamoDB: On-Demand Backup and Restore](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BackupRestore.html)
* [DynamoDB: Point-in-Time Recovery](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.html)
* [RDS: Replicating a Read Replica Across Regions](/var/folders/8_/lwswtkgd15sg92_zrbvy19qm0000gn/T/com.apple.Preview/com.apple.Preview.PasteboardItems/AWS-Reliability-Pillar (dragged).pdf)
* [S3: Cross-Region Replication](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html)
* [Route 53: Configuring DNS Failover](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring.html)
* [Amazon EBS Snapshot Copies](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-copy-snapshot.html)
* [Automating the Amazon EBS Snapshot Lifecycle](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html)
* [AMI Copies](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/CopyingAMIs.html)
* [Amazon RDS: Cross-region backup copy](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopySnapshot.html)
* [Using AWS for Disaster Recovery](https://d0.awsstatic.com/whitepapers/aws-disaster-recovery.pdf)
* [AWS Architecture Center](https://aws.amazon.com/architecture/)
* [AWS X-Ray Documentation](http://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
* [Using API Gateway to Throttle Requests](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)
* [What is AWS Systems Manager?](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)
* [Working with Deployment Groups (CodeDeploy)](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)
* [Blue/Green Deployments on AWS](https://d0.awsstatic.com/whitepapers/AWS_Blue_Green_Deployments.pdf)
* [Canary Blue/Green Deployment on ECS](https://github.com/aws-samples/ecs-canary-blue-green-deployment)
* [Blue/Green Deployment on ECS](https://github.com/awslabs/ecs-blue-green-deployment)
* [Shuffle Sharding: Massive and Magical Fault Isolation](https://aws.amazon.com/blogs/architecture/shuffle-sharding-massive-and-magical-fault-isolation/)
* [Add Scaling to Services You Build on AWS](https://aws.amazon.com/about-aws/whats-new/2018/07/add-scaling-to-services-you-build-on-aws/)


# 2. Performance Efficiency

## 2.1 Selection
### 2.1.1 Compute
#### 2.1.1.1 Documentation Resources
* [Instances: Instance Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)
* [Containers:](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_instances.html)
* [Functions:](http://docs.aws.amazon.com/lambda/latest/dg/lambda-introduction-function.html#resource-model)

### 2.1.2 Storage
#### 2.1.2.1 Documentation Resources
* [Amazon S3: Request Rate and Performance Considerations](http://docs.aws.amazon.com/AmazonS3/latest/dev/request-rate-perf-considerations.html)
* [Amazon Glacier: Amazon Glacier Documentation](http://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html)
* [Amazon EFS: Amazon EFS Performance](http://docs.aws.amazon.com/efs/latest/ug/performance.html)
* [Amazon EBS: I/O Characteristics](http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-io-characteristics.html)
* [Storage](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html)
* [EBS Storage Types](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html)
#### 2.1.2.2 Video Resources
* [Amazon EBS Design for Performance](https://www.youtube.com/watch?v=2wKgha8CZ_w)

### 2.1.3 Database
#### 2.1.3.1 Documentation Resources
* [Cloud Databases with AWS](https://aws.amazon.com/products/databases/)
* [Amazon Aurora best practices](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.BestPractices.html)
* [Amazon Redshift performance](http://docs.aws.amazon.com/redshift/latest/dg/c_challenges_achieving_high_performance_queries.html)
* [Amazon Athena top 10 performance tips](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/)
* [Amazon Redshift Spectrum best practices](https://aws.amazon.com/blogs/big-data/10-best-practices-for-amazon-redshift-spectrum/)
* [Amazon DynamoDB best practices](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices.html)
* [Amazon DynamoDB Accelerator](https://aws.amazon.com/dynamodb/dax/)



### 2.1.4 Network
#### 2.1.4.1 Documentation Resources
* [Networking Products with AWS](https://aws.amazon.com/products/networking/)

## 2.2 Review
### 2.2.1 Benchmarking
#### 2.2.1.1 Documentation Resources
* [Amazon S3 Performance Optimization](http://docs.aws.amazon.com/AmazonS3/latest/dev/PerformanceOptimization.html)
* [Amazon EBS Volume Performance](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSPerformance.html)
* [AWS CodeDeploy](https://aws.amazon.com/codedeploy/)
* [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
#### 2.2.1.2 Video Resources
* [Performance Channel](Performance Channel)
* [Performance Benchmarking on AWS](https://www.youtube.com/watch?v=sHxLpuC2CUI)


### 2.2.2 Load Testing
### 2.2.2.1 Documentation Resources
* [Load Testing CloudFront](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/load-testing.html)

## 2.3 Monitoring
### 2.3.1 Active and Passive Monitoring
### 2.3.2 Phases
### 2.3.3 Documentation Resources
* [CloudWatch Documentation](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
### 2.3.3 Video Resources
* [AWS re:Invent 2015 | (DVO315) Log, Monitor and Analyze your IT with Amazon CloudWatch](https://youtu.be/ZaOR-ybLJF0)
* [AWS re:Invent 2015 | (BDT312) Application Monitoring: Why Data Context Is Critical](https://youtu.be/aoN7bRyGA0g)


## 2.4 Tradoffs
### 2.4.1 Caching
#### 2.4.1.1 Documentation Resources
* [Best Practices for Implementing Amazon ElastiCache](http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/BestPractices.html)
* [AWS CloudFormation Best Practices](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html)
#### 2.4.1.2 Video Resources
* [Turbocharge your apps with Amazon ElastiCache](http://www.slideshare.net/AmazonWebServices/video-turbocharge-your-apps-with-amazon-elasticache)

### 2.4.2 Partitioning and Sharding
#### 2.4.2.1 Documentation Resources
* [Best Practices for DynamoDB](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices.html)
#### 2.4.2.2 Video Resources
* [AWS re:Invent 2015 | (DAT401) Amazon DynamoDB Deep Dive](https://www.youtube.com/watch?v=ggDIat_FZtA)

### 2.4.3 Compressiong
#### 2.4.3.1 Documentation Resources
* [Amazon CloudFront: Serving Compressed Files](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html)
* [Amazon RedShift: Columnar Storage](http://docs.aws.amazon.com/redshift/latest/dg/c_columnar_storage_disk_mem_mgmnt.html)
* [AWS Snowball: What Is AWS Snowball?](http://docs.aws.amazon.com/AWSImportExport/latest/ug/whatissnowball.html)

### 2.4.4 Buffering
#### 2.4.4.1 Documentation Resources
* [Best Practices for Amazon SQS](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-best-practices.html)


# 3. Security


References:
## 1.2 Foundation – Neworking
### 1.1.1 Key AWS Services
**AWS Trusted Advisor:**
### 1.1.2 Other AWS Services
The following services and features are also important: 
* **Amazon CloudWatch:**
### 1.1.3 Video Resources
[How do I manage my AWS service limits?](https://aws.amazon.com/premiumsupport/knowledge-center/manage-service-limits/)
### 1.1.4 Documentation Resources
* [AWS Service Limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)
