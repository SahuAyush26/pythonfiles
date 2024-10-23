'''
a = [2,3,4]
try:
    x = int(input("Enter value from 0-2 : "))
    print(a[x])
except ValueError:
    print("Enter a valid integer")
except IndexError:
    print("Error! Entered Integer is out of range")

print("Some important lines of code")

print("End of code")
'''

'''
# Finally keyword

def func1():
    try:
        b = int(input("Enter b : "))
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("This code will be executed because it is inside finally block even tho a value has already been returned from the above code in the function")
    
    print("This code will not be executed because a value has already been returned from the above code in the function")

l = func1()
print(l)
'''
# Raising custom errors

d = 7
try:
    c = input("Enter any integer between 5 and 9 : ")
    d = int(c)
except:
    if(c == "quit"):
       print("you good")
    else:
        raise ValueError("Enter a valid input !")

if(d<5 or d>9):
    raise ValueError("Enter a valid integer !")
elif(c == "quit"):
    print("ok fine wateva")
else:
    print("congrats ! your input was valid")
