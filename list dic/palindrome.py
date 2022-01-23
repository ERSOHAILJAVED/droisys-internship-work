# check from the string is palindrome
str=input("Enter the string : ")
temp=str
flag=False
tempLen=len(temp)
strLen=len(str)
for i in range(strLen):
    if temp[tempLen-1]==str[i]:
        flag=True
        tempLen=tempLen-1
    else:
        flag=False
        break

if flag==True:
    print('string is palindrom')
else: print('string is not palindrome')