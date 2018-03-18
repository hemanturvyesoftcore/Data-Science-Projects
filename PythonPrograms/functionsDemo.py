def swap(x,y):
    a=x
    b=y
    
    z=a+b
    a=z-a
    b=z-b
    
    print(z)
    print('the value of x is = ',a)
    print('the value of y is = ',b)
    pass

x=int(input('enter x = ') )
y=int(input('enter y = '))
swap(x, y)   