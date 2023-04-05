import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    # 수행할 함수
    p = sys.stdin.readline().rstrip()

    # 배열에 들어있는 수의 개수
    n = int(sys.stdin.readline())

    # 리스트 받아오기
    input_string = sys.stdin.readline().rstrip()
    if input_string == '[]':
        input_list = deque()
    else:
        input_list = deque(map(int, input_string.strip("[]").split(",")))

    # 반대로 직접 돌리지 않고 reverse변수를 만들어 활용

    reverse = False
    error = False

    for i in p:
        if i == 'R':
            reverse = not reverse
        elif i == 'D':
            if not input_list:
                error = True
                break
            else:
                if reverse:
                    input_list.pop()
                else:
                    input_list.popleft()

    if error:
        print("error")
    else:
        if reverse:
            input_list.reverse()
        print("[" + ",".join(map(str, input_list)) + "]")
