import sys

n, k = map(int, sys.stdin.readline().split())

num = 1

if k == 1:
    print(0)
else:
    for i in range(2, n+1):
    # n결수 만들기
        num = (((num % k) * ((10 % k) ** ((len(str(i))) % k) % k) % k)  + (i % k)) % k
    print(num)