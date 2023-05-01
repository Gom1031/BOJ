# https://www.acmicpc.net/problem/14584

import sys

amho = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())
dic = []
for i in range(n):
    dicplus = sys.stdin.readline().rstrip()
    dic.append(dicplus)

# 97이 a / f는 101


decode_dic = {'a':chr(97)}
print(decode_dic)