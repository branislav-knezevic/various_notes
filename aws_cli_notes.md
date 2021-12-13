# General

`--output JSON/text/table` type of output of the command
Output for --query is in JMESPATH
When working with `--query adding []` at the end flatterns the output
`--query 'Reservations[].Instances[].[Tags][][]`
Filtering can be done within the `[]`
`--query 'Reservations[].Instances[?VpcId = vpc-35c0275d][].[Tags]'` returns tags for all instaces with a specific VpcId
Functions can be applied to queries, eg sum() sort() sort\_by()
`sum(Reservations[]...)`
`sort_by(Contents[?Size = 2000], &LastModified).[Key.Size.LastModified]`
All queries can be set to have a result as key:value pairs
`--query 'Versions[].{Key: Key,VersionId: VersionId }'` this is an example from the s3api list-object-versions output
`aws ec2 describe-regions --output text | cut -f 3` the easiest way to get the third column of the output

## Filtering

when using `--filter` paramenter make sure to properly set the names (words devided by dashes `group-name` instad of CamelCase `GroupName`), syntax is as follows:

```bash
aws ec2 describe-security-groups --filters "Name=group-name,Values=default"
```

although in the `describe-security-groups` CamelCase is used for name `GroupName`

```JSON
{
    "SecurityGroups": [
        {
            "Description": "default VPC security group",
            "GroupName": "default",
            "IpPermissions": [
                {
                    "IpProtocol": "-1",
                    "IpRanges": [],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "UserIdGroupPairs": [
                        {
                            "GroupId": "sg-011f6d8089205f89d",
                            "UserId": "992929034856"
                        }
                    ]
                }
            ],
            "OwnerId": "992929034856",
            "GroupId": "sg-011f6d8089205f89d",
            "IpPermissionsEgress": [
                {
                    "IpProtocol": "-1",
                    "IpRanges": [
                        {
                            "CidrIp": "0.0.0.0/0"
                        }
                    ],
                    "Ipv6Ranges": [],
                    "PrefixListIds": [],
                    "UserIdGroupPairs": []
                }
            ],
            "VpcId": "vpc-0386050207ee198d2"
        },
```


# EC2

query instances from specific profile which is set in .aws/config file, with filter where Application=etcd tag exists and return private IPs along with value of Name tag
`aws ec2 describe-instances --profile go --region eu-west-1 --filters "Name=tag:Application,Values=etcd" --query 'Reservations[*].Instances[*].[PrivateIpAddress,Tags[?Key==`Name`].Value]' --output=text`

list names off all instances (if the key Name was set)
`aws ec2 describe-instances | grep '"Key": "Name"' -B 1`

get InstanceId and name of instaces
`aws ec2 describe-instances | grep '"Key": "Name"\|InstanceId' -B 1`

get names of all instances
`aws ec2 describe-instances --query 'Reservations[].Instances[].{Name:Tags[?Key==`Name`].Value}'`
`aws ec2 describe-instances --query 'Reservations[].Instances[].[Tags[?Key==`Name`].Value]' --output text`

get InstanceId or any other infor from the instance with specific name
`aws ec2 describe-instances --filter Name=tag:Name,Values=joker-worker-node-1 | grep Instance`

terminate instance based on Name Tag
`aws ec2 terminate-instances --instance-ids $(aws ec2 describe-instances --filter Name=tag:Name,Values=archimedes-sandbox-apache --query 'Reservations[].Instances[].InstanceId' --output text)`

getting specific info about the instance as a table with column names
`aws ec2 describe-instances --instance-ids i-03a7616f3c20ce78c --query "Reservations[].Instances[].{ID: InstanceId, Hostname: PublicDnsName, State: State.Name}" --output table`

use built in wait function so do while/until wouldn't be used. There is a limted number of waiters
for details chech aws ec2 wait help
this will work with the list of instances as well
```
instance_id=$(aws ec2 run-instances -image-id ami-1234 --query Reservations[].Instasnces[].InstaceId --output text)
aws ec2 wait instance-running --instance-ids $instance_id
```
simple way to get public or private IP
`aws ec2 describe-instances --instance-ids i-09429df50ffe5e04d --query "Reservations[].Instances[].PublicIpAddress` 


## Autoscaling

describe specific autoscaling group
`aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names archimedes-stage-stes-apache --profile a8s_emea`

set desired capacity, this can't be greater than the max capacity
`aws autoscaling set-desired-capacity --auto-scaling-group-name <group_name> --desired-capacity <number>`

another way to set desired and max capacity
`aws autoscaling update-auto-scaling-group --auto-scaling-group-name archimedes-stage-stes-apache --desired-capacity 2 --max-capacity 2 --profile a8s_emea`

get a current number of instances in an autoscaling group
`aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names archimedes-stage-stuk-apache --query 'length(AutoScalingGroups[].Instances)'`


## S3

copy all files from the current directory recursevly
`aws s3 cp . --profile=go s3://gtv-integration-email-templates/templates/ --recursive`

lists object in a bucket in a JSON format
`aws s3api list-objects --bucket bk-aws-test`

lists contents of a bucket in a more user friendly format 
`aws s3 ls s3://bucket_name/`


## Route53

used to create reusable domain (used to add nameservers to newly created domains)
`aws route53 create-reusable-delegation-set -caller-reference 1224`


## STS

`aws sts get-caller-identitiy` shows which user is currently logged on
