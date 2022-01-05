# # we can create the list by using list constructor

# fruitsList=list(('apple','mango','banana'))
# print(fruitsList)
# print("the length of  list : ",len(fruitsList))

box=['bindi',2,3,5,True,23,244,512,'apple',9.6]
for item in box:
    if str(item).isnumeric() and item>6:
        print(item)