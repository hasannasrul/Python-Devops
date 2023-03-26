import paramiko
import os
import time

# create ssh client
ssh = paramiko.SSHClient()

# to accept yes when asking fingerprint prompt
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# extracting key file path
relative_key_path = "../../AWS/my account resources/python-devops.pem"
absolute_key_path = os.path.abspath(os.path.join(os.getcwd(), relative_key_path))

# connect to server via ssh by passing key file path fetched above
ssh.connect(hostname=os.environ.get('EC2HOSTNAME'),username='ec2-user',key_filename=f'{absolute_key_path}')

# executing command in remote server
stdin,stdout,stderr = ssh.exec_command('cat /etc/os-release')
time.sleep(5)

# printing OP after waiting
print(stdout.readlines())

# ===================== File transfer to remote server ======================

# Writing source and destination path
source = os.path.join(os.getcwd(),'requirements.txt')
destination = '/home/ec2-user/requirements.txt'

# creating ftp client
ftp_client = ssh.open_sftp()

# uploading the file from local to remote server
ftp_client.put(source,destination)
print("uploaded")

# downloading the file from remote server to local machine (2nd argument is local machibe path)
ftp_client.get(destination, '/tmp/requirements.txt')
print("Downloaded")

# closing ssh connection
ssh.close()
