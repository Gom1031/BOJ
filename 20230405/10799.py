from collections import deque
import sys

nums = deque()

n = int(sys.stdin.readline())

for _ in range(n):
    cmd = list(map(str, sys.stdin.readline().split()))

    if cmd[0] == 'push':
        nums.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if len(nums) == 0:
            print(-1)
        else:
            print(nums.popleft())
    elif cmd[0] == 'size':
        print(len(nums))
    elif cmd[0] == 'empty':
        if len(nums) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(nums) == 0:
            print(-1)
        else:
            print(nums[0])
    elif cmd[0] == 'back':
        if len(nums) == 0:
            print(-1)
        else:
            print(nums[len(nums)-1])
