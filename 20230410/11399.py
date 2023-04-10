# i번 사람이 돈을 인출하는데 걸리는 시간 p분
# 3분 1분 4분 3분 2분 1,2,3,4,5 순서로 줄을 선다
# 2,5,1,4,3 순서로 

import sys

n = int(sys.stdin.readline())

p = list(map(int, sys.stdin.readline().split()))

p.sort()

sum = 0

for i in range(n):
    for j in p[:i+1]:
        sum += j
print(sum)