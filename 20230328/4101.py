while True:
    n, m = int(input().split())
    if n == 0 and m == 0:
        break
    elif n > m:
        print("Yes")
    else:
        print("No")
    