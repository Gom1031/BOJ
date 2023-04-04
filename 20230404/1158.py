from collections import deque

n, k = map(int, input().split())

circle = deque(range(1, n+1))

result = []

while circle:
    for _ in range(k-1):
        circle.append(circle.popleft())
    result.append(circle.popleft())

print('<' + ', '.join(map(str, result)) + '>')