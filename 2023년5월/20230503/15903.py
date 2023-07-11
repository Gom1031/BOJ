import sys
import heapq

# m번 합친다
n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
heapq.heapify(nums)

for _ in range(m):
    x = heapq.heappop(nums)
    y = heapq.heappop(nums)
    for _ in range(2):
        heapq.heappush(nums, x+y)

print(sum(nums))