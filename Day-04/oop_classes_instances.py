#Python Objet Oriented Programming

# class is a bluprint for creating instances and each unique
# student that we create using student class is an instane of the class 

#class variables are variables that are shared among all instances of a class




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


        

    


stu_1=Student('hema','Sundhar',22,66)
stu_2=Student('Test','user',21,80)
print(stu_1.first)
print(stu_2.first)


# print(stu_1.fullname())
print(Student.fullname(stu_1)) 

print(stu_1.raise_marks)

stu_1.apply_raise()
print(stu_1.marks)




print(Student.__dict__)
print(stu_1.__dict__)


Student.raise_marks=10

print(stu_1.raise_marks)
print(stu_2.raise_marks)

stu_2.raise_marks=15

print(stu_2.raise_marks)



print(Student.numofstudents)



