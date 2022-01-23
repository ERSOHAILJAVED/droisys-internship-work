# understanding decorator
def sq(num):
    return num**2
def sqrt(num):
    return num**0.5

def math(function):
    print(function(4))

math(sq)
math(sqrt)