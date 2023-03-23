import os
from datetime import datetime

def filesGreaterThanXdays(dir,n):
    print(f'==================  These files are {n} days old    =================')
    # initialise array to store file names
    arr = []
    for dirpath,subdir,files in os.walk(dir):
        for file in files:
            # check for each file in current folder
            complete_path = os.path.join(dirpath, file)

            # get file creation time in seconds
            file_creation_time_seconds = os.path.getctime(complete_path)

            # convert file creation time to timestamp
            file_creation_time = datetime.fromtimestamp(file_creation_time_seconds)

            # get current timestamp
            today_date = datetime.now()

            # get difference among above thos
            time_diff=(today_date-file_creation_time).days

            # check if difference is greater than number of days provided by user
            if time_diff > n:
                # If yes apend it to array 
                arr.append(complete_path)
                
        # print all files stored in array                 
        for i in arr:
            print(i)



if __name__=='__main__':
    print('Folder path should be absolute like /Users/hasan/Downloads')
    dirpath = input("Enter Folder Path: ")
    
    n = int(input("Enter Number of days: "))
    filesGreaterThanXdays(dirpath,n)
