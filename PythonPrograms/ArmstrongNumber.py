from math import pow

i=input('enter number = ')#string value entered
lenght=len(i)
j=int(i)
temp = j
addition=0
while temp>0:
    #print('while loop ')
    a=temp%10
    addition=int(addition+pow(a,lenght))
    temp=temp//10

if (j==addition):
    print('it is an Armstrong number : '+str(addition))
else:
    print('it is not an Armstrong Number : ')            
    
    
    
    
 
        
    
    



