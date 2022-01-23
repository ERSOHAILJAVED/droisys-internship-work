from unicodedata import name
import serialisation_Pickle,pickle

#  open a file
f=open('emp.data','wb')
n=int(input('enter the how many employ is '))
for i in range(n):
    id=int(input('enter the emp id : '))
    name=input('enter the name of employee : ')
    sal=float(input('enter the salry of employe : '))
    # creating the object emp class
    e=serialisation_Pickle.Emp(id,name,sal)
    # storeing the data 
    pickle.dump(e,f)

f.close()