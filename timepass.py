def welcome():
    print("Welcome to this place")

print("This line will be executed even when this script is imported as a module into another script and the welcome function is used in that script")

print(__name__)

if __name__ == "__main__":
    welcome() # This line will be not executed when this script is imported as a module into another script and the welcome function is used in that script

# When a script is directly executed(run), the value of __name__ is equal to "__main__"

'''
When a script1 is imported as a module into another script2 and the script1 gets executed(run)
as a result of directly running(executing) the script2, the value of __name__ is equal to "name of 
script1" and not "__main__"
'''
