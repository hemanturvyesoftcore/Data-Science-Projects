from _functools import reduce

lst=['file1.txt','file2.txt','file3.txt']

#f=open('file1.txt','r')
#print(f.readline())#to read 1 line
#print(f.readlines())

def search(x):
    count=0
    
    with open(x,'r') as f:
        for line in f:
            count+=line.count('ayub')
            pass
    return count

mapper=list(map(search,lst))
print(mapper)

var1=reduce(lambda x,y:x+y,mapper)
print(var1)

    
    
    

