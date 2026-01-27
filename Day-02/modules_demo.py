# import sys
# sys.path.append('Path...')

import My_module as mm


courses=['History','Math','Physics','Science']

index=mm.find_index(courses,"Math")

print(index)
print(mm.test)

# print(sys.path)




#######

import random

print(random.choice(courses))


######

import math

rads=math.radians(90)

sin_value=math.sin(rads)

######
import datetime
import calendar

today=datetime.date.today()
print(today)
print(calendar.isleap(2012))

####

import os

print(os.getcwd())    #cwd = current working directory


print(os.__file__)


# import antigravity

