import random as r
class Number :
    def display(self):
        l=[i**2 for i in range(r.randint(1,50))]
        print(l)

n=Number()
n.display()