import sys

# 품종 수
n = int(sys.stdin.readline())
# n 가지 품종의 색
plants = list(map(str, sys.stdin.readline().split()))
# 조수의 수 m 과 각 조수가 가진 품종의 수 k
m, k = map(int, sys.stdin.readline().split())
# m개의 줄에 걸쳐 조수가 가진 서로 다른 가지 품종의 번호
josus = []
for _ in range(m):
    josu = list(map(int, sys.stdin.readline().split()))
    josu_plant = []
    for i in josu:
        josu_plant.append(plants[i - 1])
    josus.append(josu_plant)

# 조수들중에 모두 w인게 있으면 w

result = 'P'
for i in josus:
    if 'P' in i:
        continue
    else:
        result = 'W'
        break

print(result)