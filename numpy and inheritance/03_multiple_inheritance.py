class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Employee:
    company = "Visa"
    eCode = 120


class Programmer(Freelancer, Employee):
    name = "Rohit"

p = Programmer()
print('Name is : ',p.name) # using attribute from its class
p.upgradeLevel() # using the method of parent class freelancer
print(p.company) # using the method of parent class employee