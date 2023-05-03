# import sys
# import heapq

# N = int(sys.stdin.readline())
# matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# max_heap = []
# for i in matrix:
#     for j in i:
#         # 우선순위, 값
#         heapq.heappush(max_heap, (-j, j)) 
# print(heapq.nsmallest(N, max_heap)[-1][1])




import sys
import heapq

n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

max_heap = []
for i in matrix:
    for j in i:
        heapq.heappush(max_heap, j)
        if len(max_heap) > n:
            heapq.heappop(max_heap)
print(max_heap)
print(max_heap[0])
