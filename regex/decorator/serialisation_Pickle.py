# pickle in python is used for save any thing in object format by allocating the memory differently

class Emp:
    def __init__(self,id,name,sal) -> None:
        self.id=id
        self.name=name
        self.sal=sal

    def dis(self):
        print(f'name : {self.name} id : {self.id} salary : {self.sal}')

    
