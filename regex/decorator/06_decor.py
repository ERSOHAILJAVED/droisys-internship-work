

def mydecore(func):
    def my_wrap():
        print("decorator function")
        print('functoion ',func())
        return func()
    return my_wrap


def mainFunction():
    print("main function")

mainFunction=mydecore(mainFunction)

mainFunction()