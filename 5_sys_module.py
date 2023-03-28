import sys

'''
>>  Note: It has nothing to do with your underlying OS. It is used to manipulate 
          your Python runtime environment.
          important function below
            sys.version
            sys.path
            sys.platform
            sys.argv
            sys.modules
            sys.exit()
'''
# get python version
print(sys.version)

# python will find its executable from here. just like linux uses echo $PATH
print(sys.path)

# get platform detail. in mac ot will get me kernel name which is darwin
print(sys.platform)

# get arguments from command ine
print(sys.argv)

# get all modules which is used by current python environment
print(sys.modules)

# exiting from current python module
print(sys.exit())