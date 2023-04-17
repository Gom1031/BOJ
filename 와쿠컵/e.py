import sys

d1, d2, x = map(int, sys.stdin.readline().split())
# 큰걸 d1으로 보내기
if d1 < d2:
    d1, d2 = d2, d1
print(100 / ((x/d1) + ((100-x)/d2)))