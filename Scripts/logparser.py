import os
import re
import pandas as pd

# get parent dir absolute path
parent_dir = os.path.abspath(os.path.join(os.getcwd(),os.pardir))

# regex to fetch site address
sites_pattern = r'https?:\/\/(?:www\.)?[a-z]+\.[a-z]+(?:\.[a-z]+)?'
# regex to fetch ip address
ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

# Array of document to store result
result = [
    {
    "ip": "192.168.16.23",
    "sites": ["www.google.com", 'https://www.facebook.com']
    }
]

# # open access log file as f
# with open(os.path.join(parent_dir,'dirs','sysLogs','access.log')) as f:
# # loop through each line in file
#     for line in f:
#         # declare dict to store data
#         info = {}
#         # fetch sites from current line
#         sites = re.findall(sites_pattern,line)
#         # fetch ip from current line
#         ip = re.findall(ip_pattern,line)
#         # create doc with above details and append to array
#         result.append({"ip": ip, "sites": sites})

with open(os.path.join(parent_dir,'dirs','sysLogs','access.log')) as f:
    for line in f:
        sites = re.findall(sites_pattern,line)
        ip = re.findall(ip_pattern,line)[0]
        existing_info = next((info for info in result if info["ip"] == ip), None)
        if existing_info:
            existing_info["sites"].extend(sites)
        else:
            result.append({"ip": ip, "sites": sites})

        
df = pd.DataFrame(result)
df.to_csv('logs.csv',index=False)