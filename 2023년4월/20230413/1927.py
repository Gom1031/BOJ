# `힙 자료구조 / 최소 힙을 이용
# 배열에 자연수 x 넣기
# 배열에서 가장 작은 값 출력하고, 제거
# 연산의 개수 n, 다음 n개 줄에 x
# x가 자연수라면 x 추가
# x가 0이라면 가장 작은 값 출력, 제거
# 0이 주어진 횟수만큼 답을 출력
# 배열에 비어있는데 출력하는 경우에는 0

import sys
import heapq

n = int(sys.stdin.readline())

nums = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0 and nums:
        smallest = heapq.heappop(nums)
        print(smallest)
    elif x == 0 and not nums:
        print(0)
    else:
        heapq.heappush(nums, x)