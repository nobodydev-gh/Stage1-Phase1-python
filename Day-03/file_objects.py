#File objects

#to open a file
# f=open("path" , 'r' or 'w' or 'r+' or 'a') read write read and write and append

# f=open('test.txt', 'r')

# print(f.name)

# f.close()

#########

with open('test.txt', 'r') as f:    #it will automatically close the file after exiing thius is context manager
    f_content = f.read()
    # print(f_content)
print(f.closed)


with open('test.txt', 'r') as f:    #specifing size 
    f_content = f.read(100)
    print(f_content, end='')
    f_content = f.read(100)
    print(f_content, end='')

print(f.closed)

###

# if the text is to large we cannot  print entire so we use
with open('test.txt', 'r') as f:
    size_to_read = 100
    f_content = f.read(size_to_read)

    while len(f_content) > 0:
        print(f_content, end='')
        f_content = f.read(size_to_read)




# f.tell()  # it will tell the position at where are we in the file

# f.seek(0)  # if we printed some text in the file and adn withe the seek 
# with arg 0 it will manipluate to go to the pos 0 like to the starting




with open('test.txt', 'r') as f:    
    f_content = f.readlines()       #it print all the lines
    # print(f_content)



#########
with open('test.txt', 'r') as f:    
    f_content = f.readline()   #it print  line in the file  #iterating this line will print line by line
    print(f_content, end='')  
    f_content = f.readline()   
    print(f_content, end='')

# or we can iterate
with open('test.txt', 'r') as f:

    for line in f:
        print(line, end='')


#########




###   WRITE   ###

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

### for copying a jpg

with open("file.jpg", 'rb') as rf:
    with open("file_copy.jpg", 'wb') as wf:
        for line in rf:
            wf.write(line)

        # or

with open("file.jpg", 'rb') as rf:
    with open("file_copy.jpg", 'wb') as wf:
        chunk_size =4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)

