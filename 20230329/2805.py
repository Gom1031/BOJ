import sys

n, m = map(int, sys.stdin.readline().split())

trees = []
data = sys.stdin.readline().split()
for i in data:
    trees.append(int(i))

start, end = 1, max(trees)

while start <= end:
    mid = (start+end) // 2
    count = 0
    for i in trees:
        count = count + max(i-mid, 0)
    if count >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)