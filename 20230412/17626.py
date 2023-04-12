import sys
import math

n = int(sys.stdin.readline())

nums = []

for i in range(int(math.sqrt(n)), 0, -1):
    if i**2 <= n:
        nums.append(i)
        n -= i**2
print(len(nums))