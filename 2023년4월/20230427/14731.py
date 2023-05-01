import sys

n = int(sys.stdin.readline())

sum = 0

for _ in range(n):
    c, k = map(int, sys.stdin.readline().split())
    sum += c*k*2**(k-1)

print(sum%10**9+7)