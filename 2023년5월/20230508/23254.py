# 24*n 동안 공부 가능
# 총 m개의 과목 / 시험 시간이 빠른것부터 1~m 번호
# 공부 안해도 ai점 한시간 공부할때 bi점 100점 초과 불가
# 최적의 전략으로 공부할때 최종 성적 최댓값 출력

import sys, heapq

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

n *= 24
time = 0
pq = []

# b값기준 내림차순 정렬 위해 -붙임
for i in range(m):
    heapq.heappush(pq, [-b[i], a[i]])

max = 0


while pq and n > time:
    b, a = heapq.heappop(pq)
    if (100-a)//(-b) < n - time:
        temp = a + (-b * ((100-a)//(-b)))
        if temp == 100:
            max += 100
        else:
            heapq.heappush(pq, [-(100-temp), temp])
        time += (100-a)//(-b)
    else:
        max += a + (n-time) * (-b)
        time += (n-time)
for b, a in pq:
    max += a

print(max)