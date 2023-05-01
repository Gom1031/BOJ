import math
import sys

# 어짜피 2의 곱들로 나타내니깐 log2로 계산

n = int(sys.stdin.readline())

if n == 0:
    print(0)
else:
    n = int(math.ceil(math.log2(n))+1)
    print(n)