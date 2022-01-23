# finding the prime number using the genrator
primeList=[]
num=int(input('Enter the number till where you want prime numbers : '))
def prime():
    for i in range(2,num):
        div = 0
        for j in range(1, i):
            if i % j == 0:
                div += 1
        if div == 1:
            # print(i, end=" ")
            primeList.append(i)
            # return i will not be itrable
            yield i
# prime()
sq=[i*i for i in prime()]
print('prime number list: ',primeList)
print('square of prime number list',sq)

