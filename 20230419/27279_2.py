import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

# a와 b를 내림차순으로 정렬합니다.
a.sort(reverse=True)
b.sort(reverse=True)

# b의 누적 합을 계산합니다.
b_cumsum = [b[0]]
for i in range(1, m):
    b_cumsum.append(b_cumsum[-1] + b[i])

# 가능한 x 값을 확인합니다.
for x in range(1, m + 1):
    s = b_cumsum[x - 1]
    if a[s - 1] <= m - x:
        print("NO")
        break
else:
    print("YES")
