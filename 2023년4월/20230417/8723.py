nums = list(map(int, input().split()))

max_num = max(nums)
nums.remove(max_num)
if max_num ** 2 == nums[0] ** 2 + nums[1] ** 2:
    print(1)
elif max_num == nums[0] and max_num == nums[1]:
    print(2)
else:
    print(0)