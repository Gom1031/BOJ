from collections import Counter

n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

counter = Counter(nums)
print(counter)
sorted_items = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
print(sorted_items)

if len(sorted_items) > 1 and sorted_items[0][1] == sorted_items[1][1]:
    print(sorted_items[1][0])
else:
    print(sorted_items[0][0])
