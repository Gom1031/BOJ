import sys

n, m = map(int, sys.stdin.readline().split())

listen = {}
who = []

for _ in range(n):
    name = sys.stdin.readline().rstrip()
    listen[name] = True

for _ in range(m):
    name = sys.stdin.readline().rstrip()
    if name in listen:
        who.append(name)

who.sort()

print(len(who))
for name in who:
    print(name)
