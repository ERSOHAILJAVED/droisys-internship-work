class Employee:
    company = "Google"
    salary = 100
    age=97

faiz = Employee() # object 1
happy = Employee() # object 2
happy.salary = 300  
faiz.salary = 400

print(happy.company)
print(faiz.company)
Employee.company = "YouTube" # change the attribute of class
print(happy.company)
print(faiz.company)
# if object instance attributre is given it will take it 1st than move to class
print(happy.salary) 
print(faiz.salary)
# if not given than movw to class attribute
print(happy.age)