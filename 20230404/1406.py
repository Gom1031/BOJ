from collections import deque
s = input()
s_list = deque(s)

cursor = len(s)

# m줄동안 입력할 명령어가 순서대로 주어짐
m = int(input())


for i in range(m):
    cmd = input()
    if cmd[0] == 'L':
        if cursor == 0:
            continue
        else:
            cursor -= 1
    if cmd[0] == 'D':
        if cursor == len(s_list):
            continue
        else:
            cursor += 1
    if cmd[0] == 'B':
        if cursor == 0:
            continue
        else:
            del s_list[cursor-1]
        cursor -= 1
    if cmd[0] == 'P':
        if cursor == len(s_list):
            s_list.append(cmd[2])
        else:
            s_list.insert(cursor, cmd[2])
        cursor += 1
print("".join(s_list))