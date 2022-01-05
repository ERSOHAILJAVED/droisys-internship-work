# for change in the value of tuples, 1st convert tuples into list and bck to tuples
'''
if we want change any thing inthe tuple than change into list than bck to tuple
i.e for insert del appen etc

'''

box= ("pen", "pencil", "color")
boxList=list(box)
print(boxList)
boxList.remove('pen')
boxList.append('ballpen')
box=tuple(boxList)
print(box)
