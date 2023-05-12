# 모든 노드의 깊이를 출력
# 시작정점의 깊이는 0, 방문 되지 않은 노드의 깊이는 -1
# 그래프 오름차순 방문
import sys
sys.setrecursionlimit(10**9)

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

depth = [-1] * (n+1)
count = 1

def dfs(start):
    global count
    depth[start] += count
    for i in graph[start]:
        if depth[i] < 0:
            count += 1
            dfs(i)
    count -= 1

dfs(r)

print(*depth[1:], sep='\n')