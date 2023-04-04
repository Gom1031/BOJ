while True:
    n = int(input())
    if n == 0:
        break
    reverse_int = int(str(n)[::-1])
    if reverse_int == n:
        print("yes")
    else:
        print("no")