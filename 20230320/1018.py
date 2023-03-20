import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
count_list = []
for i in range(n):
    graph.append(list(sys.stdin.readline().strip()))

# 반복회수 정하기
for i in range(n-7):
    for j in range(m-7):
        count = 0
        # 8*8로 자르기
        for k in range(i,i+8):
            for l in range(j, j+8):
                # 좌표합 짝수일때(검정색 시작 케이스)
                if (k+l) % 2 == 0 :
                    # 하얀색 아니면 +1
                    if graph[k][l] != 'W':
                        count += 1
                # 좌표합 홀수일때
                if (k+l) % 2 == 1:
                    # 검정색 아니면 +1
                    if graph[k][l] != 'B':
                        count += 1
        # count숫자를 리스트에 추가
        count_list.append(count)

# 반복회수 정하기
for i in range(n-7):
    for j in range(m-7):
        count = 0
        # 8*8로 자르기
        for k in range(i,i+8):
            for l in range(j, j+8):
                # 좌표합 짝수일때(하얀색 시작 케이스)
                if (k+l) % 2 == 0 :
                    # 검정색 아니면 +1
                    if graph[k][l] != 'B':
                        count += 1
                # 좌표합 홀수일때
                if (k+l) % 2 == 1:
                    # 검정색 아니면 +1
                    if graph[k][l] != 'W':
                        count += 1
        # count숫자를 리스트에 추가
        count_list.append(count)

print(count_list)
print(min(count_list))