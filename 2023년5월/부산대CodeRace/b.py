# 모눈종이 그림 따라그리기
# 그림 두가지 색
# 가로 방향으로만 칠할수있음
# 길이제한 x 덧칠가능
# 똑같이 그리는데 몇번 필요한지 구해보자
# 0 = 안칠해짐 / 1, 2 = 색이 칠해짐
import sys
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

count = 0

for i in graph:
    idx = 0
    while idx < m:
        if i[idx] == 0:
            idx += 1
        else:
            count += 1
            color = i[idx]
            while idx < m and i[idx] == color:
                idx += 1

print(count)