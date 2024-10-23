class Employee:
    def __init__(self,name,role):
        self.role1 = role.capitalize()
        self.name = name
        self.role = role

    def ShowDetails(self):
        print(f"{self.name} works as a {self.role} ")

class Salary(Employee):
    def Get_Salary(self):
        if(self.role1 == "Developer"):
            return f"{self.name} has a salary of Rs.70,000"
        else:
            return f"{self.name} has a salary of Rs.50,000"
        
a = Employee("Rohan", "CA")
a.ShowDetails()
# a.Get_Salary() ---> This will give error as object a belongs to class Employee and not class Salary

b = Salary("Arjun", "Developer") # This will not give error as the object b belongs to Class Salary which has inherited from class Employee
b.ShowDetails() # This will not give error as the object b belongs to Class Salary which has inherited from class Employee
print(b.Get_Salary()) 

# When a class A inherits from class B, all of the method of class B can be used on an object belonging from class A but not vice versa