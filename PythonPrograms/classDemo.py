# class demo program
class Student :
    def __init__(self,name,roll,address):
        self.name=name
        self.roll=roll
        self.address=address
        pass
    pass

stu=Student('hemant',123,'new ashok nagar')
print(stu.address)
print(stu.name)
print(stu.roll)
print(type(stu))