# nested function

from turtle import numinput


# def math():
#     def sq(num):
#         return num**2
#     print(sq(4))

# math()
def math():
    def sq(num):
        return num**2
    return sq(4)

z=math()
print(z)