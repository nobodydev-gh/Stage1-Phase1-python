

class Student:
    
    raise_marks=5

    numofstudents = 0

    def __init__(self,first,last,age,marks):
        self.first=first
        self.last=last
        self.age=age
        self.marks=marks


        Student.numofstudents+=1


    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.marks = int(self.marks + self.raise_marks)


    @classmethod
    def set_raise_marks(cls,marks):
        cls.raise_marks = marks

    @classmethod
    def from_string(cls,stu_str):
        first,last,age,marks = stu_str.split('-')
        return cls(first,last,age,marks)    


    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

stu_1=Student('hema','Sundhar',22,66)
stu_2=Student('Test','user',21,80)


Student.set_raise_marks(10)print(emp_1.email)first,last=name.split(' ')
        self.first=first
        self.last=last
print(Student.raise_marks)


stu_string_1='Rohan-Hema-22-89'

new_stu1 = Student.from_string(stu_string_1)

print(new_stu1.first)


#Statics method

import datetime
date = datetime.date(2016,7,11)

print(Student.is_workday(date))
