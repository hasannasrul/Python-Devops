import argparse
import os

# object to set description of script
parser = argparse.ArgumentParser(description='To check if file is present in folder')

# adding arguments
parser.add_argument('-d','--directory', metavar='', required=True, help='Absolute Path to folder')
parser.add_argument('-f','--file', metavar='', required=True, help='name of file')

# parsing arguments and now its available under args variable
args = parser.parse_args()


def findFile(dir,file):
    for dirPath,subfolders,files in os.walk(dir):
        if file in files:
            print('Found the file at '+ dirPath)
            return
    return 'File Not found'

if __name__=='__main__':
    d,f = args.directory, args.file
    findFile(d,f)
