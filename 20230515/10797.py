day = int(input())
cars = list(map(int, input().split()))

count = 0
for car in cars:
    if car == day:
        count += 1

print(count)
