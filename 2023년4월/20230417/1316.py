import sys

n = int(sys.stdin.readline())

count = 0

for i in range(n):
    m = str(sys.stdin.readline().rstrip())
    check = []
    group_word = True
    for j in m:
        if j in check and check[-1] != j:
            group_word = False
            break
        elif not check or check[-1] != j:
            check.append(j)
    if group_word:
        count += 1
print(count)