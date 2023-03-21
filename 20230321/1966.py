r = int(input())
for i in range(r):
    count = 0
    n, m = map(int,input().split())
    nums = list(map(int,input().split()))
    
    duplicate_nums = nums.copy()

    target = nums[m]
    nums[m] = 'target'
    
    while True:
        # nums에 한개밖에 없을때
        if len(nums) == 1:
            count += 1
            print(count)
            break

        # 맨앞이 타겟일때
        if nums[0] == 'target':
            # 타겟원래숫자가 max보다 작다면 맨뒤로
            if target < max(duplicate_nums):
                num = nums.pop(0)
                nums.append(num)
            # 타겟원래숫자가 max보다 크거나 같다면 count +1
            else:
                count += 1
                print(count)
                break

        # max랑 같다면 pop하고 count +1
        elif nums[0] == max(duplicate_nums):
            num = nums.pop(0)
            duplicate_nums.pop(duplicate_nums.index(max(duplicate_nums)))
            count += 1
        # max보다 작다면 맨뒤로
        else:
            num = nums.pop(0)
            nums.append(num)

