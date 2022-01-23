# using regex module and how to use it
import re

str='cat mat bat rat'

prog=re.compile(r'm\w\w') # an object that contains the RE 
result=prog.search(str)
# it will result but with all other info also like span for slice
print(result)
# it will only print the excat result
print(result.group())