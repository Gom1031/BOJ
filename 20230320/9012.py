from sys import stdin
n = int(stdin.readline())

for i in range(n):
    m = list(stdin.readline())
    sum = 0
    for j in m:
        if j == '(':
            sum += 1
        elif j == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')