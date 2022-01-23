# Find the max number 
numList=[]
limit=int(input('Enter the number of values that you want to enter : '))
for i in range(limit):
    print("Enter the number")
    numList.append(int(input()))
temp=numList[0]
for i in range(limit):
    if(numList[i]>temp):
        temp=numList[i]

print('list ',numList)
print('M A X number is : ',temp)
