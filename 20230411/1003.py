import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        count = [[0] * (n + 1) for _ in range(2)]

        count[0][0] = 1
        count[1][1] = 1

        for i in range(2, n + 1):
            count[0][i] = count[0][i - 1] + count[0][i - 2]
            count[1][i] = count[1][i - 1] + count[1][i - 2]

        print(count[0][n], count[1][n])
