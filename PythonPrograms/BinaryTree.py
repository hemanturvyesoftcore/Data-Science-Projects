# 1 create a Node first:

class Node:
    def __init__(self,data):
        #print('Node class called')
        self.left=None
        self.right=None
        self.data=data
# now lets insert a new Node :
    def insert(self,data):
        if self.data:
            if data  < self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif self.data:
                    if data > self.data:
                        if self.right is None:
                            self.right=Node(data)
                        else:
                            self.right.insert(data)
        else:
            self.data=data
                    
# now lets search data:
    def search(self,data):
        if self.data==data:
            return self.data
        else:
            if data < self.data:
                #print('hello')
                return self.left.search(data)
        
            else:
                return self.right.search(data)                
                    
#print all elements:
    def print_elements(self):
    #print tree content in-order
        if self.left:
            self.left.print_elements()
            print(self.data)
            
        if self.right:
                self.right.print_elements()
                print(self.data)
           
        
root=Node(8) # 1st Node object created with value = 8 
root.insert(10)
root.insert(3)
root.insert(1)
root.insert(7)
root.insert(5)
root.insert(9)

root.print_elements()
root.search(10)




