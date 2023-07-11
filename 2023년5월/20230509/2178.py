# 1은 이동할 수 있는 칸
# 0은 이동할 수 없는 칸
# 1,1 출발 n,m도착
# 최소의 칸 수 구하기
# 시작위치와 도착위치도 포함

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip()))for _ in range(n)]

result = []

def bfs(y, x):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(x, y, 1)])
    while queue:
        x, y, count = queue.popleft()

        if x == m-1 and y == n-1:
            result.append(count)
            continue
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                queue.append((nx, ny, count+1))
                graph[ny][nx] = 0

bfs(0, 0)

print(min(result))

