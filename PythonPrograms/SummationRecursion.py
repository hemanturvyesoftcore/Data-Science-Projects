# summation of numbers using Recursion

num=int(input('enter the number :'))
temp=0
def summation(n):
   
    temp=temp+n
    summation(n-1)
    return temp
        

if (num<=0):
    print(' no summation of 0 and Negative Numbers ')
else:
    print('the summation is : ')
    print(summation(num))



