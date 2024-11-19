# KG Engineers DevOps Solution

## Overview
This repository contains AWS CloudFormation templates and Python scripts for:
- AWS Infrastructure deployment (EC2, ALB, SQS)
- Beer API data retrieval and analysis

## Prerequisites
- AWS CLI installed and configured
- AWS account with appropriate permissions
- Python 3.x installed
- Python `requests` library (`pip3 install requests`)
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

### CloudFormation Stack
```bash
# Deploy New Stack
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

# Update Existing Stack
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

# Delete Stack
aws cloudformation delete-stack --stack-name interview-ec2-stack --region eu-west-1
```

### Beer API Script
```bash
# Install required Python package
pip3 install requests

# Make script executable
chmod +x beer_script.py

# Print all beers
python3 beer_script.py

# Print beers with ABV greater than 6
python3 beer_script.py 6
```

## Parameters

### CloudFormation Parameters
| Parameter | Description |
|-----------|-------------|
| VpcId | ID of the VPC where resources will be created |
| PublicSubnet1Id | ID of the first public subnet |
| PublicSubnet2Id | ID of the second public subnet |
| InstanceSecurityGroupId | Security group ID for EC2 instances |
| AlbSecurityGroupId | Security group ID for Application Load Balancer |
| InstanceType | EC2 instance type (default: t2.nano) |
| ImageId | AMI ID for EC2 instances |

### Beer Script Parameters
| Parameter | Description |
|-----------|-------------|
| ABV value | Optional numeric value to filter beers by minimum alcohol content |

## Important Notes
- CloudFormation parameter values shown are examples and should be replaced
- Ensure necessary permissions before deploying
- Review templates before deployment
- Install required Python packages before running scripts

## Clean Up
- Delete CloudFormation stack when not needed
- No cleanup needed for the Python script as it only reads data
