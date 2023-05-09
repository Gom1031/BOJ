import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

result = []


def bfs(y, x):
    queue = deque([(y, x)])  # queue 초기화

    count = 0
    while queue:
        y, x = queue.popleft()
        if 0 <= y < n and 0 <= x < n:  # y와 x의 범위를 확인
            if graph[y][x] == 1:
                graph[y][x] = 0
                count += 1

                dx = [0, 0, -1, 1]
                dy = [-1, 1, 0, 0]

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    queue.append((ny, nx))  # y, x 값을 갱신하여 추가

    return count


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(i, j))

result.sort()
print(len(result))
print("\n".join(map(str, result)))
