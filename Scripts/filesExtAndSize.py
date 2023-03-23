import os

def fileExtWithSize(extension, directory):
    for p,s,files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                print(f'file = {file}, Path = {p}')
                filePath = os.path.join(p,file)
                size = os.path.getsize(filePath)
                print(f'File size is: {size} Byte')

if __name__=='__main__':
    ext = input('Enter File Extension: ')
    dirc = input('Enter Folder name: ')
    
    fileExtWithSize(ext,dirc)