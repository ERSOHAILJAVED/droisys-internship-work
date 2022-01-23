class Empolyee:
    def __init__(self,):        
        print('i am the constructore of the employee')
    
class Freelancer(Empolyee):

    def __init__(self):
        super().__init__()
        print('i am the constructore of the freelance ')

f=Freelancer()
