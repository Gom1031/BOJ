import sys

def padovan(n, memo):
    if n <= 5:
        return memo[n]

    if memo[n] == 0:
        memo[n] = padovan(n-1, memo) + padovan(n-5, memo)
    
    return memo[n]

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    memo = [0] * (n+5)
    memo[1] = 1
    memo[2] = 1
    memo[3] = 1
    memo[4] = 2
    memo[5] = 2
    print(padovan(n, memo))
