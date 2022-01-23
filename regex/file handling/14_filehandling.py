# checking the file is present or not
from fileinput import filename
from pickle import TRUE
import clrscr,os
clrscr.clearConsole() 

filename=input("enter the file name")
z=os.path.isfile(filename+'.txt')
    
if z:
        print("press @ to stop writing ")
        with open('filename','a+') as f:
            while str!='@':
                if(str!='@'):
                    str=input()
                    f.write(str+"\n")
            f.seek(0,0)   
            print("file has following content")
            readPointer=f.read()
            print(readPointer)
else:
    print("enter the correct file name")
