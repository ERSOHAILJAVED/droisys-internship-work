# to append the data an existing file and displaying the entire file
print("press @ to stop writing ")
with open('mytext2.txt','a+') as f:
    while str!='@':
        if(str!='@'):
            str=input()
            f.write(str+"\n")

#  after writing to the file pointer will be at the end of file
#  puting at begging of file using seek()
    f.seek(0,0)
    # reading the file
    print("file has following content")
    readPointer=f.read()
    print(readPointer)





