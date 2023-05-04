# 정렬된 두 묶음 숫자카드 a, b
# 두개 합쳐서 하나로 만드는데 a+b번의 비교 필요
# 고르는 순서에 따라 비교횟수가 달라진다

import sys
import heapq

n = int(sys.stdin.readline())
min_heap = [int(sys.stdin.readline())for _ in range(n)]
min_heap.sort()
heapq.heapify(min_heap)

# 총 n-1번 연산
result = 0

while len(min_heap) > 1:
    a = heapq.heappop(min_heap)
    b = heapq.heappop(min_heap)
    result += (a+b)
    heapq.heappush(min_heap, a+b)
            
print(result)