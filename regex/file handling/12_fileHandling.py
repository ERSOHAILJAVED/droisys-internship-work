# to store group of strings in files

from asyncore import read


with open('mytext2.txt','r+') as f:
    print("Enter the string to end press @ ")
    while str!='@':
        str=input()
        if str!='@':
            f.write(str+'\n')
    readPointer=f.readline()
    print(readPointer)