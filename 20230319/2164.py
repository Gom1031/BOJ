from collections import deque

queue = deque([])

n = int(input())
for i in range(n):
    queue.append(i+1)


while True:
    if n == 1:
        print(*queue)
        break
    queue.popleft()
    if len(queue) == 1:
        print(*queue)    
        break
    else:
        m = queue.popleft()
        queue.append(m)