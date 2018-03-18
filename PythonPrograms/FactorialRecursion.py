# program to print a factorial of number by recursion method:

num=int(input('enter the number : '))

def fact(n):
    if n==0:
        return 1
    else:
        return(n*fact(n-1))
    
if num<0:
    print(' No factorial of a Negative Number ')
else:
    print('the factorial is : ')

    print(fact(num))
    
    
    

        
            





