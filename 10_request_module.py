import requests
import json
import os
import argparse


parser = argparse.ArgumentParser(description="Github api to create read and delete repo from github account ")
parser.add_argument("-r","--reponame", metavar='', help='Enter repo name')
parser.add_argument("-u","--gituser", metavar='', help='Enter github user name')

parser.add_argument("-C", "--create", action='store_true', help='Create git repository by passing repo name with -r <reponame> flag. You can also use --reponame instead of -r.')
parser.add_argument("-R", "--read" , action='store_true', help='Read all repositories present in your git account by passing -u <username> flag')
parser.add_argument("-D", "--delete" , action='store_true', help='Delete Repo present in your git account by passing -u <username> and -r <reponame> flag')

args = parser.parse_args()

token = os.environ.get("GITHUB_TOKEN")
GITHUB_API_URL = "https://api.github.com/"

## ========== Create  =============
def createRepo(reponame):
    headers = {"Authorization": "token {0}".format(token)}
    data = {"name": "{0}".format(reponame)}
    r = requests.post(GITHUB_API_URL +"user/repos" + "", data=json.dumps(data), headers=headers)
    print(r)

## ========== READ  =============
def readRepo(username):
    data = {"type": "all", "sort":"full_name", "direction": "asc"}

    output = requests.get("{0}users/{1}/repos".format(GITHUB_API_URL, username), data=json.dumps(data))
    output = json.loads(output.text)

    for reponame in output:
        print(reponame['name'])


## ========== DELETE  =============
def deleteRepo(username,reponame):
    headers = {"Authorization": "token {0}".format(token)}
    data = {"name": "{0}".format(reponame)}
    r = requests.delete("{0}repos/{1}/{2}".format(GITHUB_API_URL,username, reponame), headers=headers)
    print(r)

if __name__ == "__main__":
    if args.create:
        createRepo(args.reponame)
    elif args.delete:
        deleteRepo(args.gituser, args.reponame)
    elif args.read:
        readRepo(args.gituser)
    else:
        print("Please enter correct flags")