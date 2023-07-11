import sys
sys.setrecursionlimit(10**9)


def dfs(start, tree, parents):
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i, tree, parents)


n = int(sys.stdin.readline())

parents = [0 for _ in range(n+1)]
graph = [[]for _ in range(n+1)]

# 트리
for _ in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(1, graph, parents)

for i in range(2, n+1):
    print(parents[i])
