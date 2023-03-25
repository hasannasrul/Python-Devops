import os

### Get current Working directory
print(os.getcwd())

### Change directory
# cwd = os.getcwd()
# cd = f'{cwd}/mkdirs' 
# os.chdir(cd)
# print(os.getcwd())

### Another way of changing directory
os.chdir(os.path.join(os.getcwd(), 'dirs'))
print(os.getcwd())

### Make Directory
# os.mkdir('sysLogs')

### Better way of making directory
if not os.path.exists('sysLogs' and 'logs'):
    os.mkdir('sysLogs')
    os.mkdir('logs')
    print(os.getcwd())

### change permission of created folder
mode = 0o777
os.chmod(os.path.join(os.getcwd(), 'sysLogs'), mode)

### To create a file
os.chdir(os.path.join(os.getcwd(), 'sysLogs'))
with open('password.txt', 'w+') as f:
    f.write("USER=nasrul\nPASSWORD=root")

### Navigate to main dir
os.chdir('../../')
print(os.getcwd())

### list dir
print(os.listdir())

### get all environment variable
print(dict(os.environ))

### get particular environment variable with key
print(os.getenv('HOME'))

### get current dir path, subdir, files
print(list(os.walk(os.getcwd())))

### Get Current dir Path, subdir names, filename
for root,subdir,file in os.walk(os.getcwd()):
    print(root)
    print(subdir)
    print(file)

# to execute system level command use os.system
os.system('pwd')
os.system('ls')
os.system('uptime')
