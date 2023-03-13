import sys
t = int(input())
nums_list = list(map(int, sys.stdin.readline().split()))
count = 0
for i in nums_list:
    check = 0
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            check = 1
    if check == 0:
        count += 1
print(count)