
from builtins import int
seat={1:'Empty',2:'Empty',3:'rahul',4:'Empty',5:'Empty',6:'Empty',7:'Empty',8:'Empty',9:'Empty',10:'Empty'}
''' shows empty seats '''
class TicketBooking:
# for Displaying Empty seats
    def Show(self):
        for i in seat:
            if seat[i] ==str('Empty'):
                #BookSeat()
                print(' '+str(i)+" "+seat[i])
        
# for booking seat
    def BookSeat(self):
        print('Do you want to book seat : ?')
        if input()==int(input()):
            name=input('Insert Name :')
            seatNum=int(input('Seat Number : '))
            seat.update({seatNum:name})
            print('seat updated')
        else:
            print('Thank You for Visiting')
            exit
            #Show()
# for Booked Names and Seat Number:
    def BookedStatus(self):
        print('booked Names and Seat number are :')
        for i in seat:
            if seat[i] !=str('Empty'):
                #BookSeat()
                print('Booked Seat Number : '+str(i)+" Name: "+seat[i])
                
    
ticket=TicketBooking()
ticket.BookSeat() 
ticket.Show()
ticket.BookedStatus()
    
    
    
    
    
    
    


                
           
    