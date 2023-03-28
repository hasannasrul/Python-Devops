import requests
import json
import os

token = os.environ.get("GITHUB_TOKEN")
GITHUB_API_URL = "https://api.github.com/"

## ========== Create  =============

reponame = input("Please enter the repo name you want to create : ")
headers = {"Authorization": "token {0}".format(token)}
data = {"name": "{0}".format(reponame)}
r = requests.post(GITHUB_API_URL +"user/repos" + "", data=json.dumps(data), headers=headers)
print(r)

## ========== READ  =============

data = {"type": "all", "sort":"full_name", "direction": "asc"}

username = input("Please enter your GitHub username: ")
output = requests.get("{0}users/{1}/repos".format(GITHUB_API_URL,username), data=json.dumps(data))
output = json.loads(output.text)

for reponame in output:
    print(reponame['name'])


## ========== DELETE  =============

reponame = input("Please enter the repo name you want to delete : ")
username = input("Please enter your GitHub username: ")
headers = {"Authorization": "token {0}".format(token)}
data = {"name": "{0}".format(reponame)}
r = requests.delete("{0}repos/{1}/{2}".format(GITHUB_API_URL,username, reponame), headers=headers)
print(r)
