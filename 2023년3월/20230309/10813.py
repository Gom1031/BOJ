N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(i+1)
    
for r1 in range(M):
    i, j = map(int, input().split())
    a = arr[j-1]
    arr[j-1] = arr[i-1]
    arr[i-1] = a

print(*arr)