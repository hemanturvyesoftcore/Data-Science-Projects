#Fucktorial Number:

var=int(input('Enter Number : '))
fact=1
if var<0:
    print("not a valid number")
else:
    while (var> 1):
        fact=fact*var
        var=var-1
print('factorial is = '+str(fact))
        
        
        
        
        
        
        


