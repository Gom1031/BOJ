import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

sort_num = sorted(set(nums))

result = {value:index for index, value in enumerate(sort_num)}

for i in nums:
    print(result[i], end=' ')