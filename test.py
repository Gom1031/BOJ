import sys
from collections import deque
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in graph:
    for j in i:
        