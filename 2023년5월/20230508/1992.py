import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip()))for _ in range(n)]
def find(row, col, n):
    current = graph[row][col]
    for i in range(row, row + n):
        for j in range(col, col + n):
            if current != graph[i][j]:
                current = -1
                break
    if current == -1:
        print("(", end='')
        next = n // 2
        find(row, col, next)
        find(row, col + next, next)
        find(row + next, col , next)
        find(row + next, col + next, next)
        print(")", end='')
    elif current == 1:
        print(1, end='')
    else:
        print(0, end='')
find(0, 0, n)