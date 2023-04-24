import getpass

# this will hide the user entry in console unlike input()
passw = getpass.getpass(prompt="Enter a password: ")
print(passw)

user = getpass.getuser()
print(user)

