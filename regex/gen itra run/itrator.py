mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(myit.__next__())
print(next(myit))

