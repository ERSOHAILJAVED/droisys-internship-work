# perfoming differtent types of operations

# mixed list
mixedList=['apple','banana',343,10.5,True]
print(mixedList)
# finding form which class it is belonging
print(type(mixedList))
# printing the items through index
print(mixedList[1],mixedList[0]) 
# printing through negative index
print(mixedList[-1],mixedList[-2])
# printing through range of indexes
print(mixedList[2:4])
# printing through range of negative indexes
print(mixedList[-5:-1])
# printing value by providing onwe value
print(mixedList[1:])
print(mixedList[:])
print(mixedList[:3])
print(mixedList[-1:])
print(mixedList[:-1])
# checking the element is present in list or not
# val=input('enter the element of list')
if 343 in mixedList:
    print('element is found')
else:
    print('element not found')
# changing the value of list
mixedList[0]='papaya'
print(mixedList)
# changing the value of list with index range
mixedList[1:3]=['kiwi',455]
print(mixedList)
# inserting the elements with insert() method
mixedList.insert(2,550)
print(mixedList)
# adding the element at the end of list with append() 
mixedList.append('javed')
print(mixedList)
# extending the 1 list into another list
veg=['potato','cabage','corinder']
mixedList.extend(veg)
print(mixedList)
# removing the elements
mixedList.remove('cabage')
print(mixedList)
# removing with help of pop(),it takes index value to remove element
mixedList.pop(1)
print(mixedList)
# pop() returns the value nut del keyword doesn't
removeVal=mixedList.pop(2)
print(removeVal)
# if index value is not given then it will remove from last
mixedList.pop()
print(mixedList)
# removing the element with del keyword
del mixedList[3]
print(mixedList)
# to empty the list clear() is used
mixedList.clear()
print(mixedList)
