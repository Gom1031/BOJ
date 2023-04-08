import sys

n, k = map(int, sys.stdin.readline().split())

num = sys.stdin.readline().rstrip()

stack = []
count = 0

for i in num:
    while count < k and stack and stack[-1] < i:
        stack.pop()
        count += 1
    stack.append(i)

print(''.join(stack[:n-k]))