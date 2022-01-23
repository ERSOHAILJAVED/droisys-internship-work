# open a file with statement

with open ('mytxt.txt','r+') as f:
    f.write('my name is code and i work on computing machine \n')
    print(f.readline())
    