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
