t = int(input())

for i in range(t):
    nums = []
    k = int(input())
    n = int(input())
    floor = []
    for i in range(1,n+1):
        floor.append(i)
    nums.append(floor)
    for i in range(k):
        floor = []
        num = 0
        for j in range(n):
            num += nums[i][j]
            floor.append(num)
        nums.append(floor)
    print(nums[k][n-1])