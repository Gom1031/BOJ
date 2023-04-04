n = int(input())
nums = []
sum = 0
for i in range(n):
    m = int(input())
    if m == 0:
        nums.pop()
    else:
        nums.append(m)
for i in nums:
    sum += i
print(sum)