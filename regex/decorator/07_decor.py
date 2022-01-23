# creating two decore

def decor1(func):
    def inner():
        value=func()
        return value**2
    print(' decore1 ',inner())
    return inner

def decor2(func):
    def inner():
        value=func()
        return value*2
    print('decore2 ',inner())
    return inner

# def num():
#     return 10

# result=decor2(decor1(num))
# print(result())
@decor1
@decor2
def num():
    return 10

result=num()
print(result)

