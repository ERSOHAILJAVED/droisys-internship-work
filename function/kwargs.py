# Arbitrary Keyword Arguments, **kwargs

def addAll(**kawrgs):
    print('sum ',kawrgs['q']+kawrgs['p']+kawrgs['r'])
    


addAll(q=4,p=5,r=2)