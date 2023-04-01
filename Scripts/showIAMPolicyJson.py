import boto3
import os
import argparse
import re

parser = argparse.ArgumentParser(description='')
parser.add_argument('-p','--policyname', required=True, help='Enter policy name which json you wanna see')
args = parser.parse_args()

session = boto3.Session(aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'))
iam = session.client('iam')

## ==================== print policy json =========================

account_id = os.environ.get("AWS_ACCOUNT_ID")

# Use the client to get the policy details
response = iam.get_policy(PolicyArn='arn:aws:iam::{0}:policy/'.format(account_id) + args.policyname)

# Get the policy version details
version_response = iam.get_policy_version(
    PolicyArn='arn:aws:iam::{0}:policy/'.format(account_id) + args.policyname,
    VersionId=response['Policy']['DefaultVersionId']
)

# Get the policy JSON
policy_json = version_response['PolicyVersion']['Document']

# Print the policy JSON
print(policy_json)