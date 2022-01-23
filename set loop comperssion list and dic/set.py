utensilSet = {"pan", "cooker", "stove"}
print(utensilSet)
# Duplicate values will be ignored
utensilSet = {"pan", "cooker", "stove",'cooker'}
print(utensilSet)
# length of set
print(len(utensilSet))
# set is hetrogeous
boxSet = {"pan", 23, 40.5,True}
print(boxSet)
# set() constructor to make a set
fruitSet = set(("apple", "banana", "mango")) 
print(fruitSet)
# set doesn't follow indexes, but we can loop through to find values or etc.
true=False
for x in fruitSet:
    if x=='kiwi':
      true=True
    
if true:print("Present")
else : print("Not present")
# set are not change but elements can be added by add()
fruitSet.add("kiwi")
print(fruitSet)
# To add items from another set into the current set, use the update() method.
utensilSet.update(boxSet)
print(utensilSet)
# to remove set elemrnt we can use remove() or dicard() 
# better to use discard() bcuz it does not through any erro if element is not present
utensilSet.discard(40.5)
print(utensilSet)
utensilSet.discard(11) # 11 is not prsent in utensil
print(utensilSet)
# last element remove
utensilSet.pop()
print(utensilSet)
# empty the set clear()
utensilSet.clear()
print(utensilSet)
# delete the set del keyword
# del utensilSet
# print(utensilSet)
# union of set i.e joining both set
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) 
# The intersection_update() will keep only the items that are present in both sets.
set4={5,6,1,}
set4.intersection_update(set2)
print(set4)
# The intersection() will return new set,that only contains the items that are present in both sets.
set4={5,6,1,}
z=set4.intersection(set2)
print(z)
# symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
set4={5,6,1,}
set4.symmetric_difference_update(set1)
print(set4)
# symmetric_difference() will give new of elements that are NOT present in both sets.
w=set4.symmetric_difference(set1)
print(w)