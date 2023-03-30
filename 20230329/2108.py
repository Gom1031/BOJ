import sys
from collections import Counter

n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))

# 산술평균 구하기
sum = 0
for i in nums:
    sum += i
avg = round(sum/n)
print(avg)

# 중앙값 출력
nums.sort()
print(int(nums[n//2]))

# 최빈값 출력 / 여러 개 있을 때에는 두 번째로 작은 값 출력
counter = Counter(nums)
sorted_items = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
if len(sorted_items) > 1 and sorted_items[0][1] == sorted_items[1][1]:
    print(sorted_items[1][0])
else:
    print(sorted_items[0][0])

# 범위를 출력
print(max(nums)-min(nums))