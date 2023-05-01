import sys

n = sorted(list(map(int, sys.stdin.readline().rstrip())), reverse = True)
for i in n:
    print(i, end='')
