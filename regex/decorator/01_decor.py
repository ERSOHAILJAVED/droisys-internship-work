# define a docorator

def decor(fun):
    print('im decor')
    def inner():
        print('im inner before')
        value=fun()
        print('im inner after')
        return value+2
    return inner

@decor
def num():
    return 10

# inner_fun=decor(num)
# print(inner_fun())
print(num())
print(dir(decor))