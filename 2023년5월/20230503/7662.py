import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline())
    queue = deque()
    for _ in range(k):
        command = list(sys.stdin.readline().split())
        if command[0] == 'I':
            queue.append(int(command[1]))
        elif command[0] == 'D' and command[1] == '1' and queue:
            queue.remove(int(max(queue)))
        elif command[0] == 'D' and command[1] == '-1' and queue:
            queue.remove(int(min(queue)))

    if not queue:
        print("EMPTY")
    else:
        print(int(max(queue)), int(min(queue)))