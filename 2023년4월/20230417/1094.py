# 64cm막대 보유중
# x인 막대 가지고싶어졌음
# 모든 길이의 합이 x보다 크다면
# 가장 짧은거 절반 자르기
# 막대의 절반중 하나를 버리고 남아있는 막대의 길이합
# x보다 크거나 같다면 절반중 하나를 버린다
# 붙여서 x로 만든다다

import sys

n = int(sys.stdin.readline())

sum = 0
count = 0

for i in range(6, -1, -1):
    if 2**i <= n and sum + 2**i <= n:
        sum += 2**i
        count += 1
    if sum == n:
        break
    
print(count)