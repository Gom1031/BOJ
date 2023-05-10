import sys

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    elif n == 1:
        return 1

n, m = map(int, sys.stdin.readline().split())

print(factorial(n) // (factorial(m) * factorial(n-m)))