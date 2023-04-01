import boto3
import os

session = boto3.Session(aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'))
iam = session.client('iam')

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