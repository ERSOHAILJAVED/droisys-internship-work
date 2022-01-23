# using partial function
from functools import partial

def userDeatil(Id,domain,extension):
    print(Id+domain+extension)

email_add=input('Enter your email name only : ')
data_part=partial(userDeatil,email_add)
data_part('@gmail','.com')