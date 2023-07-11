import sys
from collections import deque
sys.setrecursionlimit(10**9)

# 지역의 높이정보 파악
# 물에 잠기지 않는 안전한 영역이 최대 몇개가 만들어지는지 조사
# 장마철에 내리는 비의 양에 따라 일정한 높이 이하 모두 물에 잠긴다
# 상하좌우

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 1 ~ 최댓값 전까지 올려가면서 확인하기
max_rain = max(max(graph)) 

visited = graph[:]

def bfs(y, x, value):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([])
    queue.append([y, x])
    visited[y][x] = 1

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] > value and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                queue.append([ny, nx])

result = 0
for i in range(max_rain):
    visited = [[0] * n for i in range(n)]
    count = 0
    for j in range(n):
        for k in range(n):
            if visited[j][k] == 0 and graph[j][k] > i:
                bfs(j, k, i)
                count += 1
    if result < count:
        result = count
    
print(result)