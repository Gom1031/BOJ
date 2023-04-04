# n = int(input())
# count = 0
# while True:
#     m = 0
#     length = len(str(count))
#     for i in range(length):
#         m += int(str(count)[i])
#     m = m + count
#     if m == n:
#         print(count)
#         break
#     else:
#         count += 1

n = int(input())
result = 0
for i in range(1, n+1):
    a = list(map(int, str(i)))
    result = i + sum(a)
    if result == n:
        print(i)
        break
    if i == n:
        print(0)