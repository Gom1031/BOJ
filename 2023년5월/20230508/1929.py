# '''
# m이상 n이하의 범위 사이 소수 하나씩 출력
# '''
# m, n = map(int,input().split())
# x = 2
# for i in range(m, n+1): #3,4,5,6,7,8...16
#     primeNum = True
#     if i == 1:
#         primeNum = False
#     else:
#         for j in range(2, i): #i = 5 / j = 1, 2, 3, 4
#             if i % j == 0:
#                 primeNum = False
#                 break
#     if primeNum:          
#         print(i)


import sys

n, m = map(int, sys.stdin.readline().split())
nums = [True] * (m + 1) 

# 에라토스테네스의 체 > 소수를 찾을때 시간 복잡도를 줄이는 방법

nums[0] = False  # 0과 1은 소수가 아니므로 False
nums[1] = False

for i in range(2, int(m**0.5) + 1):
    if nums[i]:  # i가 소수인 경우
        for j in range(i*2, m + 1, i):  
            # i의 배수를 모두 소수가 아닌 것으로 표시
            nums[j] = False

for i in range(n, m + 1):
    if nums[i]:  
        # 소수인 경우 출력
        print(i)