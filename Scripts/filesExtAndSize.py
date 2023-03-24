import os

# finds all file with given extension and its size as well
def fileExtWithSize(extension, directory):
    # initializing array to store dict objects which contains file info 
    arr = []

    # loop through all dirs
    for path,subdir,files in os.walk(directory):
        # because files is array so looping
        for file in files:
            # checking if file endswith mentioned extension
            if file.endswith(extension):
                #initiating dict to storew details of filename,path,size
                dict = {}
                # storing filename in dict object 
                dict['filename'] = file 
                # storing path of above file
                dict['path'] = path 
                # calculating size
                filePath = os.path.join(path,file)
                size = os.path.getsize(filePath)
                # storing file size
                dict['size'] = size
                # Adding dict object to array
                arr.append(dict)
    return arr

if __name__=='__main__':
    ext = input('Enter File Extension: ')
    dirc = input('Enter Folder name: ')
    
    arrOfDict = fileExtWithSize(ext,dirc)
    for doc in arrOfDict:
        print("filename = " + doc['filename'])
        print("path = " + doc['path'])
        print("size = " + str(doc['size']) + " Byte")
        print("\n")