import sys
sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, field, visited):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= len(field) or ny < 0 or ny >= len(field[0]):
            continue
        if field[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny, field, visited)

t = int(sys.stdin.readline())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    field = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        field[x][y] = 1

    count = 0
    for i in range(m):
        for j in range(n):
            if field[i][j] and not visited[i][j]:
                dfs(i, j, field, visited)
                count += 1

    print(count)
