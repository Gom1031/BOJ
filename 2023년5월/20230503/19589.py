import sys
import heapq

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
arr.sort()
min_heap = []
count = 0

for i in arr:
    while min_heap and min_heap[0] <= i[0]:
        heapq.heappop(min_heap)
    heapq.heappush(min_heap, i[1])
    count = max(count, len(min_heap))

print(count)