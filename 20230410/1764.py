import sys

n, m = map(int, sys.stdin.readline().split())

listen = set()
see = set()

for _ in range(n):
    listen.add(sys.stdin.readline().rstrip())

for _ in range(m):
    see.add(sys.stdin.readline().rstrip())

who = sorted(list(listen & see))

print(len(who))
print('\n'.join(who))