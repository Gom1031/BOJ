from sys import stdin
from collections import Counter

_ = stdin.readline()
n = stdin.readline().split()
_ = stdin.readline()
M = stdin.readline().split()

C = Counter(n)
print(' '.join(f'{C[m]}' if m in C else '0' for m in M))