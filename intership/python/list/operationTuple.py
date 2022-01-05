fruits = ("apple", "banana", "cherry")
print(fruits)
# tuples allowed duplicate elemnets bcuz of index
fruits = ("apple",'cherry', "banana", "cherry")
print(fruits)
# tuples range with index
fruits = ("apple",'cherry', "banana", "cherry")
print('range ',fruits[2:4])
# length of tuples
fruits = ("apple",'cherry', "banana", "cherry")
print(len(fruits))
#creating the single tuple, if u noty put , than it will not be a tuple
singleTuple = ("apple",)
print(singleTuple)
print(type(singleTuple))
# hetrogenous tuple
items=('apple',100,10.9,True)
print(items)
# tuple constructor
consTuple = tuple(("apple", "banana", "cherry")) 
print(consTuple)
# check elements present in tuple
box= ("pen", "pencil", "color")
if "pencil" in box:
    print("Yes, pencil in the box tuple")
# adding tuple into tuple
box2=('rubber','cutter')
box=box+box2
print(box)
# unpacking the tuple
(a,b)=box2
print(a)
print(b)
# for double the elemnts of tuples
doubleBacket = fruits * 2
print('double backret',doubleBacket)