# using the split()

import re 
def stringSplit():
    str=input('enter the string : ')
    comp=re.compile(r'\W+')
    result=comp.split(str)
    print(result)

stringSplit()