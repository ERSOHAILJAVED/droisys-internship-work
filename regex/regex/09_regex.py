# finding the words that has charcter length 4
import re

str=input(' enter the string : ')
result=re.findall(r'\b\w{5}\b',str)
print(result)