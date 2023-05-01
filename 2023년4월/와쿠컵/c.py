import sys

n = int(sys.stdin.readline())

result = 1
count = 1

while True:
    if n == 0:
        print(result-1)
        break
    if count >= n:
        print(result)
        break
    else:
        count *= 2
        result += 1