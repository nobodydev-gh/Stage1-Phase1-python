# Day 1 - Basics Proof

print("Hema Sundhar")

name = input("Enter your name: ")
print("Hello", name)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

x = 10
y = 3.14
print(type(x), type(y))

for i in range(3):
    print(i)
