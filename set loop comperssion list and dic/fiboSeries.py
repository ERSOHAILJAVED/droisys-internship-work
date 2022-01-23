# genrating the fibo series

num=int(input("Enter the no. of terms"))
a=0
b=1
print(a)
print(b)
for i in range(2,num):
    c=a+b
    a=b
    b=c
    print(c)