import sys

positions = []
count = 0

w, h, x, y, p = map(int, sys.stdin.readline().split())

for _ in range(p):
    position = list(map(int, sys.stdin.readline().split()))
    positions.append(position)

for i in range(p):
    if positions[i][0] >= x and positions[i][0] <= (x+w) and positions[i][1] >= y and positions[i][1] <= y+h:
        count += 1
    elif positions[i][0] <= x and positions[i][0] >= (x-h/2) and positions[i][1] >= y and positions[i][1] <= (y+h) and ((x - positions[i][0])**2 + ((y+h/2) - positions[i][1])**2) ** 0.5 <= h/2:
        count +=1
    elif positions[i][0] >= (x + w) and positions[i][0] <= (x + w + h/2) and positions[i][1] >= y and positions[i][1] <= (y + h) and ((positions[i][0] - (x + w))**2 + ((y + h/2) - positions[i][1])**2) ** 0.5 <= h/2:
        count += 1

print(count)