# finding the words starting with a

import re
str=input("enter the string that atleast contains two words of a : ")
# if don't use \b it will print any character that starts with a
# result=re.findall(r'a[\w]*',str)
result=re.findall(r'\ba[\w]*\b',str)
for i in result:
    print(i)
print(result)