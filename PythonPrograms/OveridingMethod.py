# Overriding means same functions name
class Parent:
    def __init__(self):
        print('parent class __init__ called')
        
    def Fun(self):
        print('this is a Parent Class')
        super().Fun()
    pass
class Child(Parent):
    
    def __init__(self):
        print('child class __init__ called')
        #super().__init__()
        
    def Fun(self):
        super().__init__()###
        print('this is a Child Class')
        
    pass
    
obj=Child()
print(obj.Fun())