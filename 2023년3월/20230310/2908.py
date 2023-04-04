num1, num2 = map(list, input().split())
num1.reverse()
num2.reverse()

num1 = int(''.join(num1))
num2 = int(''.join(num2))

if num1 > num2:
    print(num1)
elif num1 < num2:
    print(num2)
else:
    print(num1)