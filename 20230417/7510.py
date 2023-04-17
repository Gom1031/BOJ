import sys

t = int(sys.stdin.readline())

for i in range(t):
    nums = list(map(int, sys.stdin.readline().split()))
    max_num = nums.pop(nums.index(max(nums)))
    if max_num ** 2 == nums[0] ** 2 + nums[1] ** 2:
        result = "yes"
    else:
        result = "no"
    print("Scenario #%d:" %(i+1))
    print(result)
    print('')