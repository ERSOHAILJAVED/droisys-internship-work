# list compression
x1=[1,2,67,9]
numList=[x*x for x in x1]
print(numList)

# list compression to genrate squares of list
sqList=[x*x for x in range(1,11)]
print(sqList)
# list compression to genrate cube of list
cubeList=[pow(x,3) for x in range(1,11)]
print(cubeList)
# list compression to genrate cube listof even numbers
cubeList=[pow(x,3) for x in range(1,11) if x%2==0]
print(cubeList)