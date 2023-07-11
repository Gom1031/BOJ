import sys
import heapq

t, n = map(int, sys.stdin.readline().split())
# id / 필요시간 / 우선순위
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

pq = []

# 우선순위를 음수로 바꾸어 저장
for item in arr:
    # 우선순위(음수) / id / 필요시간
    heapq.heappush(pq, (-item[2], item[0], item[1]))

while t > 0:
    priority, proc_id, time_left = heapq.heappop(pq)
    if time_left == 0:
        continue

    print(proc_id)
    heapq.heappush(pq, (priority + 1, proc_id, time_left - 1))
    t -= 1