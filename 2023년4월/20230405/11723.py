import sys

m = int(sys.stdin.readline())

s = []

for _ in range(m):
    you = sys.stdin.readline().split()
    if you[0] == 'add':
        if you[1] in s:
            continue
        else:
            s.append(you[1])
    elif you[0] == 'remove':
        if you[1] in s:
            s.remove(you[1])
        else:
            continue
    elif you[0] == 'check':
        if you[1] in s:
            print(1)
        else:
            print(0)
    elif you[0] == 'toggle':
        if you[1] in s:
            s.remove(you[1])
        else:
            s.append(you[1])
    elif you[0] == 'all':
        s = [str(i) for i in range(1, 21)]
    elif you[0] == 'empty':   
        s = []
