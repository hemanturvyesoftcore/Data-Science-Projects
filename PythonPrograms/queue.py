from collections import deque
queue = deque ([1,2,3,4,5,6,7])

queue.appendleft(89)
queue.append(77)

print(queue)
print(type(queue))
print(type(deque))
