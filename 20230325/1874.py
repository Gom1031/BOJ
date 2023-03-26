#숫자 n개
n = int(input())

nums = []
for i in range(n):
    nums.append(int(input()))

compare = []
for i in range(1,nums[0]+1):
    compare.append(i)
print(compare)