def hanoi(n, start, mid, end):
    if n == 1:
        print(start, end)
    else:
        hanoi(n-1, start, end, mid)
        print(start, end)
        hanoi(n-1, mid, start, end)

n = int(input())
if n <= 20:
    print(2**n-1)
    hanoi(n, 1, 2, 3)
else:
    print(2**n-1)