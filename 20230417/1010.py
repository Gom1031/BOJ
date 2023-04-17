# 동쪽과 서쪽으로 나누는 큰 일직선 강
# 서쪽에는 n개의 사이트 / 동쪽에는 m개의 사이트
# 다리를 지을 수 있는 경우의 수를 구하는 프로그램

import sys
import math

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(math.factorial(m) // (math.factorial(n) * math.factorial(m-n)))