# class Dog:
#     def talk(self):
#         print ("bark")
# dog1 = Dog()
# dog1.talk()  # --> Bark

# def cat_talk(self):
#     print ("Meow")

# Dog.talk = cat_talk
# dog1.talk()  # --> Meow

# importing the module
from types import FunctionType
  
# functttion during run-time
f_code = compile('def gfg(): return "GEEKSFORGEEKS"', "<string>", "exec")
f_func = FunctionType(f_code.co_consts[0], globals(), "gfg")
z=f_code.co_consts[0]
print(z)  
# calling the function
print(f_func())
print(type(f_code))
print(type(f_func))
