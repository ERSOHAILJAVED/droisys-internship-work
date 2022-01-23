# writing and reading from file

filehandler=open('mytxt.txt','w')
str=input('enter the content for file : ')
filehandler.write(str)
filehandler.close()
f=open('mytxt.txt','r')
str1=f.read()
print(str1)
f.close()