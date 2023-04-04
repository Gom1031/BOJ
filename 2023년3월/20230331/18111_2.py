import sys

n, m, b = map(int, sys.stdin.readline().split())
height_count = [0] * 257

for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for h in row:
        height_count[h] += 1

min_time = float('inf')
final_height = 0

for height in range(257):
    if height_count[height] == 0:
        continue

    time = 0
    blocks_needed = 0
    blocks_removed = 0

    for h in range(257):
        if height_count[h] == 0:
            continue

        diff = h - height
        if diff > 0:
            blocks_removed += diff * height_count[h]
            time += 2 * diff * height_count[h]
        elif diff < 0:
            blocks_needed -= diff * height_count[h]
            time -= diff * height_count[h]

    if blocks_removed + b >= blocks_needed:
        if time <= min_time:
            min_time = time
            final_height = height

print(min_time, final_height)
