import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

nums = [0 for _ in range(10002)] 
for i in range(len(a)):
    nums[i] = a[i]
count = 0

for i in range(1000):
    if nums[i+1] > nums[i+2]:
        temp = min(nums[i], nums[i+1]-nums[i+2])
        nums[i] -= temp; nums[i+1] -= temp;
        count += temp * 5

        temp2 = min(nums[i], nums[i+1], nums[i+2])
        nums[i] -= temp2; nums[i+1] -= temp2; nums[i+2] -= temp2;
        count += temp2 * 7        
    else:
        temp2 = min(nums[i], nums[i+1], nums[i+2])
        nums[i] -= temp2; nums[i+1] -= temp2; nums[i+2] -= temp2;
        count += temp2 * 7

        temp = min(nums[i], nums[i+1])
        nums[i] -= temp; nums[i+1] -= temp;       
        count += temp * 5
    count += nums[i] * 3

print(count)
