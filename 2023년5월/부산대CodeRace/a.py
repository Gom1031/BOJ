# 첨탑 밀어서
# 앞에서 밀면 뒤로 넘어진다
# 넘어지는 탑 높이가 다음 높이보다 클때만 밀린다
# 총 몇번 밀어야하는지 계산

import sys

n = int(sys.stdin.readline())
h_list = list(map(int, sys.stdin.readline().split()))

count = 1

for i in range(len(h_list)-1):
    if h_list[i] > h_list[i+1]:
        continue
    else:
        count += 1

print(count)