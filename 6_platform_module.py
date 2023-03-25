import platform

'''
>>   A platform module is used to access underlying platform data such as operating system,
     interpreter version information, and hardware.
'''

# Will return name of operating system equivalent of "uname" in linux terminal 
print(platform.system())

# will show achitecture of system like 64bit
print(platform.architecture())

# return machine type in mac it is arm64
print(platform.machine())

# return kernel information
print(platform.uname())

# return relase version of kernel
print(platform.release())

# retutn pythhon version 
print(platform.python_version())