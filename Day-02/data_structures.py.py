# Lists


courses =['History','Math','Physics','Science']

print(courses)

print(len(courses))  

print(courses[2])  #to print specific value at the index

print(courses[-2])

print(courses[1:3])

#To add an  item to our list 
courses.append("Art")  # Add at the end of the list
print(courses)

#To insert item at a specific position
courses.insert(1,'orange')
print(courses)


#list in list

l1=['History','Math','Physics','Science']
l2=['Art','Orange']

l1.insert(0,l2)
print(l1)

#add the l2 to l1
l1.extend(l2)
print(l1)


courses1 =['History','Math','Physics','Science']

# Remove a value from the list
popped=courses1.pop()   # remove the vale at the last index
print(popped)  #prints the popped value


print(courses1)

courses1.remove('Math') # remove value 





courses2 =['History','Math','Physics','Science']

#Reverse the list
courses2.reverse()
print(courses2)


#To sort the list

apha=['f','w','p','a']

apha.sort()

print(apha)

nums=[4,2,6,1,3,5]

nums.sort()
print(nums)

#to make sort and reverse

nums1=[4,2,6,1,3,5]
nums1.sort(reverse=True)
print(nums1)








#Sort the list but the original list should be not be altered

apha=['t','d','b','a']

sorted_courses=sorted(apha)

print(apha)
print(sorted_courses)



num3=[6,3,7,5,1,2,4]

print(min(num3))    #Want minimum value in the list

print(max(num3))    #maximun vakue in the list

print(sum(num3))    #sum of all the numbers i the list



#To find the index of a value
courses3 =['History','Math','Physics','Science']

print(courses3.index('Math'))  #returns the index of the value
print('Math' in courses3) # To check the value is in the list or not  returns True



for item in courses3:
    print(item)


for index,item in enumerate(courses):
    print(index,item)

for index,item in enumerate(courses, start=1):
    print(index,item)




#convert list into string and join
course_str = ' - '.join(courses3)
print(course_str)

#To convert str to list

new_list=course_str.split(' - ')
print(new_list)


empty_list = []
#or
empty_list = list()







# Tuples
...
#Tuples        We cannot modify Tuples      but we can modify lists
#So Tuples are  Immutable

tuple_1 = ('History','Math','Physics','Science')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0]='Art'

#we cannot append add insert cannot  do anythying



#tuples
empty_list = ()
#or
empty_list = tuple()







# Sets

#Sets         the values that are unordered and prints with no duplicates

Sets_1 = {'History', 'Math', 'Physics', 'Science', 'Math'}
Sets_2 = {'Commerce', 'Math', 'Physics', 'Biology', }

print(Sets_1)
print(Sets_2)

#To check the common values in the 2 sets
print(Sets_1.intersection(Sets_2))  #prints the common value in both

#print the courses that are not in the other set

print(Sets_1.difference(Sets_2))


print(Sets_1.union(Sets_2))



#Sets
empty_set = {}  #this is not a set this is dictionary

empty_list = set()






# Dictionaries
...


#dictinonary_1 ={key : value}

student = {'name': 'Rohan','age': 21,'courses':['Math','Science']}

print(student)

print(student['courses'])

print(student['name'])

print(student.get('phone','Not Found'))

#adding

student['phone'] ='01234'


#update

#student['name'] = 'Hema'

        #or

student.update({'name':'ITACHI','age': 20})

print(student)


#DELETING

del student['age']
print(student)

    #or
phone=student.pop('phone')
print(phone)
print(student)



#to print no of keys

print(len(student))

#print the keys

print(student.keys())

#print the values

print(student.values())

#to print keys and values
print(student.items())



#loop through the dictionary

for key in student:
    print(key)

for key,value in student.items():
    print(key, value)