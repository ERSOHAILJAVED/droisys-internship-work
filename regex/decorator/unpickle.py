import serialisation_Pickle,pickle
# open file
f=open('emp.data','rb')
print('Employess details : ')
while True:
    try:
        # read a file from objects
        obj=pickle.load(f)
        # display the content
        obj.dis()
    except EOFError:
        print('file is ended ')
        break

f.close()