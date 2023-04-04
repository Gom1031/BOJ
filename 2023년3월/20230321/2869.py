import sys
# a만큼 올라가고 b만큼 떨어지고 높이가v
a, b, v = map(int, sys.stdin.readline().split())
count = (v-b) / (a-b)
print(int(count) if count == int(count) else int(count)+1)