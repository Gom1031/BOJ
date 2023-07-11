# 친구 n명 r개의 라운드
# 점수 계산은 상근이와 친구 개개인을
# 2, 1, 0점

import sys
# a가 상근 b가 친구
def RSP_count(a, b):
    if a == 'R':
        if b == 'R':
            return 1
        elif b == 'S':
            return 2
        elif b == 'P':
            return 0
    elif a == 'S':
        if b == 'R':
            return 0
        elif b == 'S':
            return 1
        elif b == 'P':
            return 2
    elif a == 'P':
        if b == 'R':
            return 2
        elif b == 'S':
            return 0
        elif b == 'P':
            return 1

r = int(sys.stdin.readline())
sang = list(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline())
friend = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
RSP = ['R', 'S', 'P']

cnt = 0
cnt_max = 0

# 상근이가 친구들이랑 해서 나온 결과
for i in range(r):
    for j in friend:
        cnt += RSP_count(sang[i], j[i])

# 최댓값 찾기
for i in range(r):
    temp = [0, 0, 0]
    for j in range(n):
        for k in range(3):
            result = RSP_count(RSP[k], friend[j][i])
            temp[k] += result
    cnt_max += max(temp)

print(cnt)
print(cnt_max)