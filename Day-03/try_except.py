try:
    f = open('test.txt')
    var=bad_var
except FileNotFoundError:                       # or except FileNotFoundError as e
    print('Sorry!.File not exist')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Exceuting finally!")
##############################

try:
    f = open('test1.txt')
    if f.name == 'test1.txt':
        raise Exception
except FileNotFoundError:                       # or except FileNotFoundError as e
    print('Sorry!.File not exist')
except Exception as e:
    print(e)


##########################
# Error Handling Basics

try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)

except ValueError:
    print("Invalid input. Please enter a number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except Exception as e:
    print("Unexpected error:", e)

else:
    print("No errors occurred.")

finally:
    print("Execution finished.")
