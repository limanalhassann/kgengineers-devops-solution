# KG Engineers DevOps Solution

## Overview
This repository contains AWS CloudFormation templates for deploying infrastructure as code. The solution includes EC2 instances, Application Load Balancer, and associated resources.

## Prerequisites
- AWS CLI installed and configured
- AWS account with appropriate permissions
- Basic understanding of AWS services and CloudFormation

## Authentication Setup
Configure your AWS CLI with credentials:

```bash
aws configure
```

You will be prompted to provide:
- AWS Access Key ID
- AWS Secret Access Key
- Default region
- Default output format

## Deployment Instructions

### Deploy New Stack
```bash
aws cloudformation create-stack \
    --stack-name interview-ec2-stack \
    --template-body file://KGDevOpsInterview.json \
    --capabilities CAPABILITY_IAM \
    --parameters \
        ParameterKey=VpcId,ParameterValue=vpc-04cd45b40f61b024e \
        ParameterKey=PublicSubnet1Id,ParameterValue=subnet-04989bd16f72efafa \
        ParameterKey=PublicSubnet2Id,ParameterValue=subnet-0aa2a700b0e3cd546 \
        ParameterKey=InstanceSecurityGroupId,ParameterValue=sg-0099033da5b0fba62 \
        ParameterKey=AlbSecurityGroupId,ParameterValue=sg-0099033da5b0fba62 \
        ParameterKey=InstanceType,ParameterValue=t2.nano \
        ParameterKey=ImageId,ParameterValue=ami-047bb4163c506cd98
```

### Update Existing Stack
```bash
aws cloudformation update-stack \
    --stack-name interview-ec2-stack \
    --template-body file://KGDevOpsInterview.json \
    --capabilities CAPABILITY_IAM \
    --parameters \
        ParameterKey=VpcId,ParameterValue=vpc-04cd45b40f61b024e \
        ParameterKey=PublicSubnet1Id,ParameterValue=subnet-04989bd16f72efafa \
        ParameterKey=PublicSubnet2Id,ParameterValue=subnet-0aa2a700b0e3cd546 \
        ParameterKey=InstanceSecurityGroupId,ParameterValue=sg-0099033da5b0fba62 \
        ParameterKey=AlbSecurityGroupId,ParameterValue=sg-0099033da5b0fba62 \
        ParameterKey=InstanceType,ParameterValue=t2.nano \
        ParameterKey=ImageId,ParameterValue=ami-047bb4163c506cd98
```

### Delete Stack
```bash
aws cloudformation delete-stack --stack-name interview-ec2-stack --region eu-west-1
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| VpcId | ID of the VPC where resources will be created |
| PublicSubnet1Id | ID of the first public subnet |
| PublicSubnet2Id | ID of the second public subnet |
| InstanceSecurityGroupId | Security group ID for EC2 instances |
| AlbSecurityGroupId | Security group ID for Application Load Balancer |
| InstanceType | EC2 instance type (default: t2.nano) |
| ImageId | AMI ID for EC2 instances |

## Important Notes
- Parameter values shown are examples and should be replaced with your actual values
- Ensure you have necessary permissions before deploying
- Review the CloudFormation template before deployment

## Clean Up
To avoid unwanted charges, remember to delete the stack when no longer needed using the delete command provided above.

