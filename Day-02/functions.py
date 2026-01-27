def hello_func():
    pass

print(hello_func())

####
def hellow():
    print("Hello World")

hellow()


for i in range(4):
    hellow()


####

def hW():
    return "Hello World!"

print(hW())

print(hW().upper())
print(hW().lower())

####

def greet(greeting,name='You'):
    return '{} {}.'.format(greeting,name)

print(greet("Hi",name="Rohan"))

####



def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math','Art', name="Rohan",age=21)

####


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

course = ['Math', 'Art']
info = {'name': 'Rohan', 'age':21}

student_info(*course,**info)


# Example

def is_leap(year):
    return year % 4 == 0 and (year % 100 !=0 or year % 400 == 0 )

####


month_days=[0,31,28,31,30,31,30,31,30,31,30,31]



def days_in_months(year,month):

    if not 1 <= month <=12 :
        return 'Invalid month'
    
    if month == 2 and is_leap(year):
        return 29

    return month_days[month] 



print(is_leap(2020))

print(days_in_months(2020,2))