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

count = 0
count2 = 0
time = 0

for i in sum:
    count += (mode_value - i)
if count >= 0:
    # 인벤토리에서 값이 부족하지 않으면 가능
    if b >= count:
        if count == 0:
            sys.exit()
        else:
            print(count, mode_value)
            raise SystemExit

# 인벤토리에서 값이 부족하면 탈출
for i in sum:
    # 땅파기
    count2 += (i - min(sum))
time = count2 * 2
print(time, min(sum))    