#use of function and return keyword in a class
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age= age
        pass
    def Display(self):
        return(print('Students name is '+self.name+' and his age is '+str(self.age)))
    pass
student1=Student('bob',16)
student1.Display()