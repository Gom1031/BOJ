import sys

n = int(sys.stdin.readline().rstrip())

nums = list(map(int, sys.stdin.readline().split()))
right = []
left = []

# right에 nums 모두 추가
for i in nums:
    right.append(i)

result = []

for _ in range(n):
    count = 0
    for i in left:
        if i >= right[0]:
            count = nums.index(i) + 1
    result.append(count)
    left.append(right.pop(0))
print(*result)