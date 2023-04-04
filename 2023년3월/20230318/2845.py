n, m = map(int, input().split())
nums = list(map(int, input().split()))

people = n * m
result = []
for i in nums:
    result.append(i - people)
print(*result)