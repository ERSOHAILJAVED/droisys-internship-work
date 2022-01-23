list = [1,2,3,4,5,6,7]  
  
# List Comprehension  
z = [x**2 for x in list]  
  
# Generator expression  
a = (x**2 for x in list)  
  
print(a.__next__())  
print(a.__next__())  
print(a.__next__())  
print(a.__next__())  
print(a.__next__())  
print(a.__next__())  
print(a.__next__())  
print(z) 