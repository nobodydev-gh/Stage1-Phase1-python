import os

print(dir(os)) #lists all the attribute and methods of this module

print(os.getcwd()) #print current working directory

os.chdir("/home/rohan/DEV/")    # change the directory

print(os.getcwd())  


print(os.listdir())     #Lists all the folders in the cwd





os.mkdir("OS_demo1/")   # create folder in working directory 

print(os.listdir()) 





os.makedirs("os_demo/demo1")  #create folder and also sub folders in the directorys

print(os.listdir()) 




os.rmdir("OS_demo")  # delete the folder only  (will not intermediate directories)



os.removedirs("os_demo/demo1")    #delete the sub folder       (will intermediate directories)




os.remame("original_file_name","changed_file_name")





os.rename("OS_demo1","OS_demo")  # rename the file or folder







print(os.stat('OS_demo'))  #print info about the file or folder






from datetime import datetime
mod_time=os.stat('OS_demo').st_mtime
print(datetime.fromtimestamp(mod_time))






#all directories files and paths from the path 

for dirpath, dirnames, filenames in os.walk('/home/rohan/DEV'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()


#to find file exist or not 
os.path.exists("path")


#to find that it is directory or not

os.path.isdir('path')

#for file
os.path.isfile('path')





os.path.splitext('/tmp/test.txt')   









