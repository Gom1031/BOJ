import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort(reverse=True)
b.sort(reverse=True)

b_cumsum = [b[0]]
for i in range(1, m):
    b_cumsum.append(b_cumsum[-1] + b[i])

for x in range(1, m + 1):
    s = b_cumsum[x - 1]
    if a[s - 1] <= m - x:
        print("NO")
        break
else:
    print("YES")
