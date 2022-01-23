# using the findall() function it gives all result in list

import re

def compile():
    prog=re.compile(r'm\w\w')
    return prog

def stringFind():
    str=input("enter the string : ")
    # compile()    
    result=compile().findall(str)
    print(result)
if __name__=='__main__':
    stringFind()