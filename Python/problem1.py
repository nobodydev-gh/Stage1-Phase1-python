#print all the files in the directory by the specified path

import os

directory_path= '/'

contents= os.listdir(directory_path)

for item in contents:
    print(item)


