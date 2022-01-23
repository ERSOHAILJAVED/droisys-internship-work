# import the module from add1.py
from cmath import e


try:
    from .mod.add1 import add
    def div():
        a=int(input('enter the  num for div'))
        b=int(input('enter the  num for div'))
        print('div is : ',a/b)
        add()
except Exception as e:
    print('Module path is not finding..... check its path and try again')
    print(e)