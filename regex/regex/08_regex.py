# to get words that starts with number
import re
from unittest import result
str='the meeting is start will be conducted on 1st and 21st of every month'
result=re.findall(r'\d[\w]*',str)
print(result)