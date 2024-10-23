class employee:
    def __init__(self,name,occupation):
        self.name = name
        self.occupation = occupation

    def info(self):
        print(f"{self.name} is a {self.occupation}") 

a = employee("Ayush", "Engineer")
b = employee("Harry", "Accountant")

a.info()
b.info()
