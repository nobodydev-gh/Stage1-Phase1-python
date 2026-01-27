#Interger
n=3

#Float
m=3.14

# to find the type of data stored in a variable 
print(type(n))  
print(type(m))

# Arithmetic operations

print(3 + 2)    #Addition 

print(3 - 2)    #Subtraction

print(3 * 3)    #Multiplication

print(3 / 2)    #Division

print(3 % 2)    #Modulus

print(3 ** 2)   #Exopnent

print(3 // 2)   #floor division



num=1

num+=1
print(num)

#Built in function

print(abs(-3))     #absolute value

print(round(3.75))  #Round value

print(round(3.75,1)) #Round the value to the first digit after the decimal



#Comparision
print(3==2)  #Equal

print(3!=2)  #Not Equal

print(3 > 2)  # Greater Than

print(3 < 2)  # Less Than

print(3 >= 2) # Greater or Equal

print(3 <= 2) # Less than or Equal




#Type Casting

num1='100'     #this is a Stringn not integer
num2='200'      

print(num1 + num2)  #It will concatinate the Strings adn result is 100200  it will not add

#to add the number which are in string we convert them into integer data type

num1= int(num1)
num2= int(num2)
print(num1 + num2)  #result 300

num