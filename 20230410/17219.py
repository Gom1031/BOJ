# 비밀번호를 찾는 프로그램
# 저장된 사이트 주소의 수 n 비밀번호를 찾으려는 사이트 주소의 수 m
# n줄에 걸쳐 각 주루에 사이트 주소와 비밀번호
# 그 후 비밀번호를 찾으려는 사이트 주소 입력

import sys

n, m = map(int, sys.stdin.readline().split())

site = {}

for _ in range(n):
    p, q = map(str, sys.stdin.readline().split())
    site[p] = q

for _ in range(m):
    name = str(sys.stdin.readline().rstrip())
    print(site[name])