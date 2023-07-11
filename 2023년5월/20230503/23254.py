# 24*n 시간 공부가능
# 과목 총 m가지
# 시험 시간이 빠른 과목부터 1~m 번호
# 최저 0점 최고 100점

# i번 과목에서 a점 받는다 한시간할때마다 b점 올린다
# 100점 초과 불가

import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
n *= 24
a_list = list(map(int, sys.stdin.readline().split()))
b_list = list(map(int, sys.stdin.readline().split()))
max_heap = []
for i in range(m):
    heapq.heappush(max_heap,[-up_score[i],score[i]])

time = 0
result = 0
while max_heap and time < n*24:
    find = heapq.heappop(max_heap)
    if not max_heap or (100 - find[1]) % (-find[0]) >= (-max_heap[0][0]):
        result += 100
        time += (100 - find[1]) // (-find[0]) + 1
    else:
        result += (100 - find[1]) // (-find[0]) * (-find[0])
        time += (100 - find[1]) // (-find[0]) 

print(result)