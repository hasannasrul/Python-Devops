import paramiko
import os
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

relative_path = "../../AWS/my account resources/python-devops.pem"
absolute_path = os.path.abspath(os.path.join(os.getcwd(), relative_path))

ssh.connect(hostname='3.239.199.223',username='ec2-user',key_filename=f'{absolute_path}')
stdin,stdout,stderr = ssh.exec_command('cat /etc/os-release')
time.sleep(5)
print(stdout.readlines())
ssh.close()