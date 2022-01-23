def div(a,b):
    return a/b

def smartfunc(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
    return inner

a=2;b=4
if a>b:
   print(div(a,b))
else:
    # using decorator
    div1=smartfunc(div)
    print(div1(a,b))

