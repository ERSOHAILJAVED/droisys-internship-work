# creating the class for cal. area

class Area:
    def cal(self):
        print('area of circle ')
        r=float(input("Enter the radius "))
        a=3.14*r*r
        print('Area of circle is: ',a,'sq.unit')


a=Area()
a.cal()

