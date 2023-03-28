import boto3
import os

'''
In Boto3, there are two ways to interact with Amazon Web Services (AWS) resources:

1. client
2. resource object.

1.  The client object provides a low-level interface to AWS services.
    It communicates directly with the AWS APIs and returns the raw data
    in the form of Python dictionaries. 

2.  Resources abstracts away the details of the underlying API calls and provides a simpler,
    more Pythonic interface. It is modeled after AWS resources and allow you to perform 
    actions on them using Python methods.

'''

# create session 
session = boto3.Session(aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'), aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'))

# create client / resource
iam = session.client('iam')

# list all iam user
userResponse = iam.list_users()

# list all iam groups 
groupResponse = iam.list_groups()

print("========  Users present in your account are: =============")
for user in userResponse['Users']:
    print(user['UserName'])

print("========  Groups present in your account are: =============")
for group in groupResponse['Groups']:
    print(group['GroupName'])


## ======================== code to list all self created iam policy =======================

# Use the client to list all IAM policies
response = iam.list_policies(Scope='Local')

# Create a list to hold the ARNs of your manually created policies
policy_arns = []

# Iterate over the policies and append the ARNs of your manually created policies to the list
for policy in response['Policies']:
    if policy['IsAttachable'] and policy['Path'] == '/' and policy['Arn'].split(':')[-1].split('/')[0] == 'policy':
        policy_arns.append(policy['Arn'])

# Use the client to get the details of each manually created policy
print("========  policies created by you are: =============")
for policy_arn in policy_arns:
    policy = iam.get_policy(PolicyArn=policy_arn)
    print(policy['Policy']['PolicyName'], policy['Policy']['Arn'])


## ==================== print policy json =========================

account_id = os.environ.get("AWS_ACCOUNT_ID")
policy_name = input("Enter Policy name: ")

# Use the client to get the policy details
response = iam.get_policy(PolicyArn='arn:aws:iam::{0}:policy/'.format(account_id) + policy_name)

# Get the policy version details
version_response = iam.get_policy_version(
    PolicyArn='arn:aws:iam::{0}:policy/'.format(account_id) + policy_name,
    VersionId=response['Policy']['DefaultVersionId']
)

# Get the policy JSON
policy_json = version_response['PolicyVersion']['Document']

# Print the policy JSON
print(policy_json)