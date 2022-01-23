# using the group function when its gives none

import re
from unittest import result
str="cat pat bat rat"
prog=re.compile(r'm\w\w')

result=prog.search(str)

if result is not None:
    print(result.group())
else: 
    print("string is not there")