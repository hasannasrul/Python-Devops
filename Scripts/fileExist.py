import os

def doesExist(dirc, fname):
    for root, dirs, files in os.walk(dirc):
        if fname in files:
            print("File Exist at", os.path.join(root, fname))
            return os.path.join(root, fname)
    print("File Not Exist")

if __name__=='__main__':
    print('EG - /root/yourdir ')
    dirc = input("Enter Folder in which you want to find file : ")
    fname = input("Enter FILE NAME: ")
    doesExist(dirc,fname)
