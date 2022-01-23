# count number of words line and character

with open("mycount.txt",'a+') as f:
    print(" press @ to stop writing ")
    
    while str!='@':        
        if str!='@':
            str=input()
            f.write(str+'\n')
    f.seek(0,0)
    # counting the lines words and char
    cl=cw=cc=0
    for line in f:
        # print(line)
        line=line.strip('\n')
        # strip() remove the character that you don't want in string
        if line!='@' and line!=" ":
            cl+=1
            words=line.split()
            cw+=len(words)
            # print(words)
            cc+=len(line)
        


print("lines ",cl)
print("words ",cw)
print("char ",cc)
