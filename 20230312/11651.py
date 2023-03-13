n = int(input())
positions = []
for i in range(n):
    coordinate = list(map(int, input().split()))
    positions.append(coordinate)
positions.sort(key=lambda x: (x[1], x[0]))
for i in positions:
    print(i[0], i[1])