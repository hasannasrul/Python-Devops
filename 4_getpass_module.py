import getpass

passw = getpass.getpass(prompt="Enter a password: ")
print(passw)

user = getpass.getuser()
print(user)