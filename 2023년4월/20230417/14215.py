import sys

nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
hap = nums[0] + nums[1]
if hap <= nums[2]:
    print(nums[0] + nums[1] + hap-1)
else:
    print(sum(nums))