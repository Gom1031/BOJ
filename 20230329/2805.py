import sys

# n, m = map(int, sys.stdin.readline().split())

# trees = list(map(int, sys.stdin.readline().split()))

# start, end = 1, max(trees)

# while start <= end:
#     mid = (start+end) // 2
#     count = 0
#     for i in trees:
#         count = count + max(i-mid, 0)
#     if count >= m:
#         start = mid + 1
#     else:
#         end = mid - 1
# print(end)

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start, end = 0, max(trees)
result = 0

while start <= end:
    mid = (start+end) // 2
    count = sum([i-mid for i in trees if i > mid]) # mid값 보다 큰값들만 i-mid 계산
    if count >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)