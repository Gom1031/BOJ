# 양수, +, -, 괄호로 식만들고 > 괄호를 모두 지웟다
# 괄호를 적절히 쳐서 식을 최소로 만들기
# 처음과 마지막은 숫자
# 5자리보다 연속되는 숫자는 없다
# 수는 0으로 시작할수있다

a = input().split('-')

num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)