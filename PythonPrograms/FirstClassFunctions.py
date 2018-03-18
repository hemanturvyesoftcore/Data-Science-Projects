#Properties of first class functions:
'''A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists,'''

# normal function

def square(x):
    return x*x

def cube(x):
    return x*x*x

f=square(5) # here the f is equal to the value return by the square function 
print(f)
print(square)

#1->You can store the function in a variable.

f=square # here the f is equal to the function itself just by removing the (). basically having () means executing a function

print(f)#but, by removing the () we have assigned the function to a variable .which automatically is behaves like function itself.
print(square)

print(f(7))#now we can treat variable f as square().

#2--> You can pass the function as a parameter to another function.

def MyMap(func,arg_list):
    result=[]
    for i in arg_list:
        result.append(func(i))
    return result

squares=MyMap(square, [1,2,3,4,5])#here square() is used as an argument in the MyMap()

print(squares)

squares=MyMap(f, [1,2,3,4,5])
print(squares)

cubes=MyMap(cube, [1,2,3,4,5])#here cube() is used as an argument in the MyMap()
print(cubes)

#3 --> You can return the function from a function.

def first(a):
    def second():
        print('Urvey : ',a)
    return second # here we are only returning object of second(),Not executing it.

b=first('Hemant ')
print(b())



        


        

    








