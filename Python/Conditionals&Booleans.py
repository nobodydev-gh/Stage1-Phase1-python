
if True :
    print("True")


language ='java'

if language == 'python':
    print('LANGUAGE IS PYTHON')

elif language == 'java':
    print("Language is java")
else:
    print("No match")


user='Admin'
login=True

if user == 'Admin' and login:
    print("Success")
else:
    print("Failed")


if user == 'Admin' or login:
    print("Success")
else:
    print("Failed")


if not login:
    print("Success")
else:
    print("Failed")


a=[1,2,3]
b=[1,2,3]
print(a == b)

print(id(a))
print(id(b))
print(a is b)  # due to the id of a and b are not same


# 0=False
# 1=True

#False Values
# None
# Zero of any numeric type
# Any empty sequence example: ',(),[].
# Any empty mapping  example: {}.
