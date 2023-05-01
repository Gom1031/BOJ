import sys

# 숫자 n개와 합이 s가 되는 부분수열의 개수를 출력
n, s = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

n = len(nums)
result = []

# 비트마스킹으로 모든 부분수열의 합 result에 저장
for i in range(2**n):
    subset_sum = 0
    for j in range(n):
        if i & (1 << j) != 0:
            subset_sum += nums[j]
    result.append(subset_sum)

count = 0

for i in result:
    if i == s:
        count += 1

# 0일때는 공집합 빼주기
if s == 0:
    count -= 1

print(count)