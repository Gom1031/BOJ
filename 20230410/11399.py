import sys

n = int(sys.stdin.readline())

p = list(map(int, sys.stdin.readline().split()))

p.sort()

sum = 0

for i in range(n):
    for j in p[:i+1]:
        sum += j
print(sum)