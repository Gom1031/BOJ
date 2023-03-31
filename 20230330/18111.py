import sys
from collections import Counter

n, m, b = map(int,sys.stdin.readline().split())
block = []
for i in range(n):
    block.append(list(map(int, sys.stdin.readline().split())))

# 모든 값 하나의 리스트로 합치기
sum = [i for sublist in block for i in sublist]
# 최빈값 찾기
mode_value = Counter(sum).most_common(1)[0][0]

print(mode_value)

count = 0
time = 0
for i in block:
    for j in i:
        count = mode_value - j
    if count > 0:
        if b > count:
            continue



