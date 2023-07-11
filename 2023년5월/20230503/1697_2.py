import sys
from collections import deque

def dfs(n):
    graph = deque([n])
    while graph:
        search = graph.popleft()
        if search == k:
            return time[search]
        else:
            for next_search in (search-1, search+1, search*2):
                if 0 <= next_search < max and not time[next_search]:
                    graph.append(next_search)
                    time[next_search] = time[search] + 1


max = 100001
time = [0] * max
n, k = map(int, sys.stdin.readline().split())
print(dfs(n))