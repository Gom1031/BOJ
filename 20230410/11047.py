# n종류 동전 많이
# 합을 k로 만드려고 한다
# 필요한 동전 개수의 최솟값을 구하는 프로그램

import sys

n, k = map(int, sys.stdin.readline().split())

coin = []
count = 0

for _ in range(n):
    coin.append(int(sys.stdin.readline().rstrip()))

coin.reverse()

for i in coin:
    if k // i == 0:
        continue
    else:
        count += k // i
        k -= i * (k//i)
print(count)
