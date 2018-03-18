var=int(input('enter the year = '))
if (var%4==0):
    print('it is a Leap Year : '+str(var))
else:
    if (var%400==0):
        print('it is a Leap Year : '+str(var))
        
    else:
        print('it is not a leap year : '+str(var))
    