import sys

count = 0
count_list = []
n = int(sys.stdin.readline())
topping = list(map(str, sys.stdin.readline().split()))
for i in topping:
    if "Cheese" == i[-6:] and i not in count_list:
        count += 1
        count_list.append(i)
if count >= 4:
    print("yummy")
else:
    print("sad")