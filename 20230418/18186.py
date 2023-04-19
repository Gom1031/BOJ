import sys

n, b, c = map(int,sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

nums = [0 for _ in range(1000002)] 
for i in range(len(a)):
    nums[i] = a[i]
count = 0

for i in range(n):
    if b <= c:
        count += nums[i] * b
    else:
        if nums[i+1] > nums[i+2]:
            temp = min(nums[i], nums[i+1]-nums[i+2])
            nums[i] -= temp; nums[i+1] -= temp;
            count += temp * (b+c)

            temp2 = min(nums[i], min(nums[i+1], nums[i+2]))
            nums[i] -= temp2; nums[i+1] -= temp2; nums[i+2] -= temp2;
            count += temp2 * (b+2*c)        
        else:
            temp2 = min(nums[i], min(nums[i+1], nums[i+2]))
            nums[i] -= temp2; nums[i+1] -= temp2; nums[i+2] -= temp2;
            count += temp2 * (b+2*c)

            temp = min(nums[i], nums[i+1])
            nums[i] -= temp; nums[i+1] -= temp;       
            count += temp * (b+c)
        count += nums[i] * b

print(count)
