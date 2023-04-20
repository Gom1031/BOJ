import sys

n = sys.stdin.readline().rstrip()

count = 0
i = 0

while i < len(n):
    if i < len(n) - 1:
        if n[i:i+2] in ('c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z='):
            count += 1
            i += 2
        elif i < len(n) - 2 and n[i:i+3] == 'dz=':
            count += 1
            i += 3
        else:
            count += 1
            i += 1
    else:
        count += 1
        i += 1

print(count)
