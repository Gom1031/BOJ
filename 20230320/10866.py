from collections import deque
import sys

nums = deque()
n = int(sys.stdin.readline())
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push_front":
        nums.insert(0, command[1])
    if command[0] == "push_back":
        nums.append(command[1])
    if command[0] == "pop_front":
        if len(nums) == 0:
            print(-1)
        else:
            print(nums.popleft())
    if command[0] == "pop_back":
        if len(nums) == 0:
            print(-1)
        else:
            print(nums.pop())    
    if command[0] == "size":
        print(len(nums))
    if command[0] == "empty":
        if len(nums) == 0:
            print(1)
        else:
            print(0)
    if command[0] == "front":
        if len(nums) == 0:
            print(-1)
        else:
            num = nums.popleft()
            print(num)
            nums.appendleft(num)
    if command[0] == "back":
        if len(nums) == 0:
            print(-1)
        else:
            num = nums.pop()
            print(num)
            nums.append(num)
