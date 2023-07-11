# 40점 미만은 항상 40점
result = 0
a = [int(input()) for _ in range(5)]
for i in a:
    if i < 40:
        result += 40
    else:
        result += i
print(int(result/5))
