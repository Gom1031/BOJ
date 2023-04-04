N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(0)

for r1 in range(M):
    i, j, k = map(int, input().split())
    for r2 in range(i-1, j):
        arr[r2] = k

print(*arr)