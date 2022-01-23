# sorting by sorting method
fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits.sort()
print(fruits)
# sorting in reverse in order
fruits.sort(reverse=True)
print(fruits)
# sort() 1st sort the Capital letters
fruits2 = ["orange", "Mango", "kiwi", "pineapple", "Banana"]
fruits2.sort()
print(fruits2)
# using the reverse() to reverse the order without alphabetic sort
fruits2.reverse()
print(fruits2)
# copying the list from one to another
newList=fruits2.copy()
print(newList)
# concatenate of 2 or more strings
newList=fruits2+fruits
print(newList)