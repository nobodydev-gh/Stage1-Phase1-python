import datetime

d = datetime.date(2005,2,25)
print(d)


#local date
today=datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)




print(today.weekday())          #Monday 0    Sunday 6
print(today.isoweekday())       #Monday 1    Sundat 7




#########################################################

# timedelta = the difference between two dates or time
tdelta = datetime.timedelta(days=7)

# print the date one week from now
print(today + tdelta)

#print the date one week ago
print(today - tdelta)

#########################################################



t=datetime.time(9,30,45,100000)
print(t)
print(t.hour)




td=datetime.datetime(2088,3,26,12,30,45,10000)
print(td)