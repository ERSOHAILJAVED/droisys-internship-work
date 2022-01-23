# non-local variable and closure function in Python
# num is local variable of math() but it is used by sq() also,that's y sq() is closer function
def math(num):
    def sq():
        return num**2
    return sq()

z=math(4)
print(z)