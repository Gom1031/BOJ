import sys

s = input()
left_stack = list(s)
right_stack = []

# m줄동안 입력할 명령어가 순서대로 주어짐
m = int(input())

for _ in range(m):
    cmd = sys.stdin.readline().rstrip()
    if cmd[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    if cmd[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    if cmd[0] == 'B':
        if left_stack:
            left_stack.pop()
    if cmd[0] == 'P':
        left_stack.append(cmd[2])

# 결과 문자열을 출력합니다.
print("".join(left_stack + right_stack[::-1]))
