import sys

n, m = map(int, sys.stdin.readline().split())

# 포켓몬 이름을 저장할 딕셔너리와 리스트를 생성합니다.
name_to_number = {}
number_to_name = [None] * n

for i in range(n):
    name = sys.stdin.readline().rstrip()
    name_to_number[name] = i + 1
    number_to_name[i] = name

# m개의 질문에 대해 처리합니다.
for _ in range(m):
    query = sys.stdin.readline().rstrip()

    if query.isdigit():  # 질문이 숫자인 경우
        print(number_to_name[int(query) - 1])
    else:  # 질문이 이름인 경우
        print(name_to_number[query])