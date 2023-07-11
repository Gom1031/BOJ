# 1은 집있는거 0은 집없는거
# 연결된 집의 모임인 단지를 정의, 단지에 번호붙이기
# 연걸 > 상하좌우
# 단지수를 출력하고 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력

import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip()))for _ in range(n)]

result = []
queue = deque([(y, x, 1)])

def bfs(y, x):
    while queue and 0 <= y < n and 0<= x < n:
        temp = []
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        y, x, count = queue.popleft()
        if graph[y][x] > 0:
            count += graph[y][x]
            for i in range(4):
                temp.append(count)
                queue.append((y + dy, x + dx, count))
        else:
            reuslt.append(max(temp))
            for i in range(4):
                queue.append((y + dy, x + dx, 0))

bfs(0, 0)
print(len(result))
print(i for i in result)