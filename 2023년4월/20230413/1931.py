# 한개의 회의실/ n개의 회의에 대하여 회의실 사용표
# 시작시간, 끝나는 시간이 주어져있다
# 각 회의가 겹치지 않게 회의의 최대 개수
# 시작시간과 끝나는시간이 같을 수 있다
# 회의 수 n / 각 줄마다 공백을 사이에 두고 시작시간 / 끝나는 시간
# 회의 최대 개수 출력

import sys

n = int(sys.stdin.readline())
times = []
for _ in range(n):
    time = list(map(int, sys.stdin.readline().split()))
    times.append(time)

# 종료시간을 기준으로 정렬하되, 종료시간이 같을 경우 시작시간을 기준으로 정렬
times.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

for time in times:
    if time[0] >= end_time:
        count += 1
        end_time = time[1]

print(count)
