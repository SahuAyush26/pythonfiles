class employee:
    name = "Ayush"
    occupation = "Engineer"

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = employee()
a.info()
b = employee()
b.name = "Harry"
b.occupation = "Accountant"
b.info()