# @staticmethod is used when we want to it should be called for every object/instance

class Employee:
    company = "Google"
    salary=500

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

happy = Employee()
happy.salary = 100000
happy.getSalary("Thanks!") # Employee.getSalary(happy)
happy.greet() # Employee.greet()
happy.time()

