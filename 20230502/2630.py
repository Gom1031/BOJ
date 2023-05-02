import sys

# white, blue / 0이면 하얀색 1이면 파란색

n = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = []

def reculsion(x, y, n):
    color = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != graph[i][j]:
                reculsion(x, y, n//2)
                reculsion(x, y+n//2, n//2)
                reculsion(x+n//2, y, n//2)
                reculsion(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

reculsion(0, 0, n)

print(result.count(0))
print(result.count(1))