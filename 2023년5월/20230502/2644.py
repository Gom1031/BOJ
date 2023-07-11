import sys

# 총 사람의 수
n = int(sys.stdin.readline())

# 찾을 두 사람
p, q = map(int, sys.stdin.readline().split())

# 관계 갯수
m = int(sys.stdin.readline())

graph = [[]for _ in range(n+1)]
visited = [False] * (n+1)
result = []

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

#####

def dfs(v, count):
    count += 1
    visited[v] = True

    if v == q:
        result.append(count)
    for i in graph[v]:
        if not visited[i]:
            dfs(i, count)

dfs(p, 0)

if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)