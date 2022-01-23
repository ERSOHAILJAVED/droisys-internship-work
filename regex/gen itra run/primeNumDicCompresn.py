# finding the prime number using the genrator and dictonary compression
primeList=[]
num=int(input('Enter the number till where you want prime numbers : '))
def prime():
    for i in range(2,num):
        div = 0
        for j in range(1, i):
            if i % j == 0:
                div += 1
        if div == 1:           
            primeList.append(i)           
            yield i
sq=[i*i for i in prime()]
primeDict={primeNum:sqPrime for primeNum,sqPrime in zip(primeList,sq)}
print(primeDict)

