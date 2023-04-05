# r뒤집기 d버리기

import sys


t = int(sys.stdin.readline())
for _ in range(t):
    # 수행할 함수
    p = sys.stdin.readline().rstrip()

    # 배열에 들어있는 수의 개수
    n = int(sys.stdin.readline())

    # 리스트 받아오기
    input_string = sys.stdin.readline().rstrip()
    if input_string == '[]':
        input_list = []
    else:
        input_list = list(map(int, input_string.strip("[]").split(",")))

    for i in p:
        if i == 'R':
            input_list.reverse()
        if i == 'D':
            if len(input_list) == 0:
                input_list.append('error')
                break
            else:
                input_list.pop(0)
    if isinstance(input_list[0], str):
        print(*input_list)
    else:
        print("[" + ",".join(map(str, input_list)) + "]")