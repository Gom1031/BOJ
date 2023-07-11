import sys

sum = 0

for _ in range(4):
    sum += int(sys.stdin.readline())

print(sum // 60)
print(sum % 60)