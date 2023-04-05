import sys

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))

stack = []
result = [0] * n

for i, h in enumerate(nums):
    while stack and nums[stack[-1]] < h:
        stack.pop()
    if stack:
        result[i] = stack[-1] + 1
    stack.append(i)

print(*result)