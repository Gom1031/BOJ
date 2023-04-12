import heapq
import sys

n = int(sys.stdin.readline())

nums = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0 and nums:
        largest = -heapq.heappop(nums)
        print(largest)
    elif x == 0 and not nums:
        print(0)
    else:
        heapq.heappush(nums, -x)