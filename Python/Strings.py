#print Hello World!
print("Hello World!")


#create Variable and print data in it

message='Bob\'s World'
print(message)

#to find length of the variable
print(len(message))

#print letter at specific position
print(message[10])


#print only required word
print(message[0:6])

print(message[6:])


# methods

print(message.lower())


print(message.upper())

#count certain number of characters
print(message.count('o'))
print(message.count('World'))


#Find index of some word
print(message.find("World"))


#Replace some characters

message=message.replace('World','Universe')
print(message)


#concatinate

greeting = 'Hello'
name = 'Rohan'

message= greeting + name

message1 = greeting + ', ' + name

message2 = greeting + ', ' + name + '. Welcome!'

print(message)

print(message1)

print(message2)


new = '{}, {}. Wlecome!'.format(greeting,name)

print(new)
