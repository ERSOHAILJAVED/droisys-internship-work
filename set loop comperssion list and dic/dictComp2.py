# dictionary compression for creating new dict.
# items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
dict={'a':1,'b':2,'c':3,'d':4}
dictCube={key:value**3 for (key,value) in dict.items() }
print(dictCube)
# using power function
dict={'a':1,'b':2,'c':3,'d':4}
dictCube={key:pow(value,3) for (key,value) in dict.items() }
print(dictCube)