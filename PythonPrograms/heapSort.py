from _heapq import heappush, heappop
def heapsort(data):
    h=[]
    
    for value in data:
        heappush(h,value)
    return [heappop(h) for i in range(len(h))]
    
x=heapsort([1,7,4,0,3,8,2,6])
print(x)
print(heapsort([1,7,4,0,3,8,2,6]))
