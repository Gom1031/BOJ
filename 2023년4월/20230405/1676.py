import math
import sys

n = int(sys.stdin.readline())
result = list(str(math.factorial(n)))

count = 0

for i in result[::-1]:
    if i == '0':
        count += 1
    else:
        print(count)
        break
