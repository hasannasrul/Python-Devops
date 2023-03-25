import re
import os

# pattern to match ip address
pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

with open(os.path.join(os.getcwd(),'dirs','logs','ip.txt')) as ipfile:
    content = ipfile.read()

match = re.findall(pattern, content)

print("==== All ip address in file are ====")
for i in match:
    print(i)

# ====================== pattern to match ip address ======================

'''
Below Pattern Explanation 

1. character prior to ? means it is optional
2. \ used for escape sequence
3. [a-z] means any character from alphabets
4. + means it may occur one time or more
5. don't forget to escape . by adding / prior to it
'''

pattern = r'https?:\/\/(?:www\.)?[a-z]+\.[a-z]+(?:\.[a-z]+)?'

with open(os.path.join(os.getcwd(),'dirs','logs','sites.txt')) as ipfile:
    content = ipfile.read()
    
match = re.findall(pattern, content)

print("==== All sites address in file are ====")
for i in match:
    print(i)