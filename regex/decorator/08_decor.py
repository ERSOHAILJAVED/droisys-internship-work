def add(a,b):
    print('sum : ',a+b)
    return None

def div(func):
    def inner_div(a,b):
        
        return a/b
    return inner_div


print(add(2,4))

calling=div(add)
print('div : ',calling(2,4))

