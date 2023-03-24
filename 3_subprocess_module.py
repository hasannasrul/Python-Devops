import subprocess

# command which you want to execute
cmd = 'ls -lrt'

''' 
>> .Popen() is a method which is used to execute shell command

>>  shell=True means it will execute command in new opened shell and 
    if false it will run commands as ['ls' '-lrt'] means treat them as list and run in 
    same python process so its little fast. only drawback of shell=False will be it will not
    run env variables commands correctly. like ['echo', '$HOME']. 

>>  stdout=subprocess.PIPE is used to capture stdout output in the variable

>>    universal_newlines=True will treat output as string and not as Bytecode 
''' 
sp = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)

# it will wait till command is executed and return 0 if executed successfullly or non zero otherwise.
sc = sp.wait()

# send input to the process
stdout,stderr = sp.communicate()

print(f'Output - {stdout}')
print(f'Output - {stdout.splitlines()}')
print(f'Error - {stderr}')
print(f'Error - {stderr.splitlines()}')