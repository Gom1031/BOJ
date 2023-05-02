import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
  dx = [1, 1, -1, -1, 1, -1, 0, 0]
  dy = [0, 1, 0, 1, -1, -1, 1, -1]

  graph[x][y] = 0
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
      dfs(nx, ny)

while True:
    count = 0
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    graph = []
    for _ in range(h):
        n = list(map(int, sys.stdin.readline().split()))
        graph.append(n)
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                count += 1

    print(count)