import sys

m = int(sys.stdin.readline())

s = 0

for _ in range(m):
    command = sys.stdin.readline().split()
    if command[0] == 'add':
        # s의 command[1] 번째 비트를 1로 설정함
        s |= 1 << int(command[1])  
    elif command[0] == 'remove':
        # s의 command[1] 번째 비트를 0으로 설정
        s &= ~(1 << int(command[1]))
    elif command[0] == 'check':
        if s & (1 << int(command[1])):
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        s ^= 1 << int(command[1])
    elif command[0] == 'all':
        s = (1 << 21) - 1
    elif command[0] == 'empty':
        s = 0

