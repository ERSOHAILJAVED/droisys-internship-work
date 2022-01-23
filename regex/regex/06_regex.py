# using the sub() to find and repalce with new string
import re
from turtle import st
def stringSplit():
    str=input('enter the string : ')
    result=re.sub(r'mat','cat',str)
    print(result)
stringSplit()