N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(i+1)
for r in range(M):
    i, j = map(int, input().split())
    arr[i-1:j] = arr[i-1:j][::-1]
print(*arr)