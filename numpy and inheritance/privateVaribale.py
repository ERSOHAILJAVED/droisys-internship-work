
class School:
    __phoneno=123456789 #private  variable 
    # protected 
    _roll=123

    def __display(self):
        print('diaplay mobile number from inside class ',School.__phoneno)
    
    def publicfun(self):
        print('displaying from public fun ',)
        self.__display()

sc=School()
print(sc._roll)
sc.publicfun()
