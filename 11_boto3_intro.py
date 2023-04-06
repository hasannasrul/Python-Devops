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

