# handling the multiple exception
def avg(list):
    total=0
    for x in list:
        total+=x

    avg=total/len(list)
    return total,avg

try:
    t,a=avg([1,2,3,4,5])
    print(f' total = {t}, average{a}')
except TypeError:
    print('type error plz provide the number in lists')
except ZeroDivisionError:
    print('dont pass the empty lists')

