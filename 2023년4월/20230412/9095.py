import sys

def count(n):
    dp = [0] * (n+1)
    if n <= 2:
        return n
    elif n == 3:
        return 4
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    dp[n] = count(n-1) + count(n-2) + count(n-3)
    return dp[n]
n = int(sys.stdin.readline())
for _ in range(n):
    m = int(sys.stdin.readline())
    print(count(m))