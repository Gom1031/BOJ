import sys

nums = list(map(int, sys.stdin.readline().split()))
nums2 = nums[:]
nums3 = nums[:]
for i in range(3):
    result = []
    while True:
        nums.sort()
        if nums[0] ** 2 + nums[1] ** 2 >= nums[2] ** 2:
            result.append(sum(nums))
            break
        else:
            nums[0] -= 1
    while True:
        nums2.sort()
        if nums2[0] ** 2 + nums2[1] ** 2 >= nums2[2] ** 2:
            result.append(sum(nums2))
            break
        else:
            nums2[1] -= 1
    while True:
        nums3.sort()
        if nums3[0] ** 2 + nums3[1] ** 2 >= nums3[2] ** 2:
            result.append(sum(nums3))
            break
        else:
            nums3[2] -= 1
print(result)