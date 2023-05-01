import sys
import math

n = int(sys.stdin.readline())

# 1의 제곱수로만 이루어진 경우
if int(math.sqrt(n))**2 == n:
    print(1)
else:
    # 두 개의 제곱수의 합으로 이루어진 경우
    for i in range(1, int(math.sqrt(n)) + 1):
        if int(math.sqrt(n - i * i))**2 == n - i * i:
            print(2)
            break
    else:
        # 세 개의 제곱수의 합으로 이루어진 경우
        for i in range(1, int(math.sqrt(n)) + 1):
            temp = n - i * i
            for j in range(1, int(math.sqrt(temp)) + 1):
                if int(math.sqrt(temp - j * j))**2 == temp - j * j:
                    print(3)
                    break
            else:
                continue
            break
        else:
            # 네 개의 제곱수의 합으로 이루어진 경우
            print(4)
