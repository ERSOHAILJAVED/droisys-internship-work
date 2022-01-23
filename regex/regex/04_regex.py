# using the match() that search at begging of string only

import re
import regex03 as reg
comp=reg.compile()

def searchString():
    str=input("enter the string that starts with M : ")
    result=comp.match(str)
    # print(result.group())
    print(result)

searchString()