# i 가 n+1개
# o 가 n개
# 가 교대로 나오는 문자열을 pn
# i, o 로만 이루어진 문자열 s와 n이 주어졋을때
# s안에 pn이 몇군데 포함되어있는지

import sys

n = int(sys.stdin.readline())
pn = []
for i in range(2*n+1):
    if i % 2 == 1:
        pn.append('O')
    else:
        pn.append('I')

m = int(sys.stdin.readline())
s = list(sys.stdin.readline().rstrip())
visited = []
count = 0
for i in s:
    visited.append(i)
    if len(visited) >= len(pn):
        if visited[-(len(pn)):] == pn:
            count += 1
print(count)