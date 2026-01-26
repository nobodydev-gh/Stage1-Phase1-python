
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