import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
check = False

for i in range(1, n):
    count = 0
    vita_front = s[:i]
    vita_back = s[n-i:]

    for a, b in zip(vita_front, vita_back):
        if a != b:
            count += 1
    if count == 1:
        check = True
        break

print("YES" if check else "NO")