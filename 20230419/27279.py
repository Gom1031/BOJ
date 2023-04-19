import sys

n, m = map(int, sys.stdin.readline().split())
a = sorted(list(map(int, sys.stdin.readline().split())))
b = sorted(list(map(int, sys.stdin.readline().split())))

check = [None] * n
j = 0
for i in a:
    if i == m:
        continue
    else:
        check[j] = b[:i]
    j += 1

for i in range(m):
    for j in range(i+1, len(check)):
        if check[j] is None:
            break
        else:
            check[j][i] -= check[i][i]

all_zero = False

for i in check:
    if all(x == 0 for x in i):
        all_zero = True
        break
if all_zero:
    print("NO")
else:
    print("YES")