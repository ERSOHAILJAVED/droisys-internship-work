#  how self work in classes
class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

happy = Employee()
happy.salary = 100000
happy.getSalary() # Employee.getSalary(happy)