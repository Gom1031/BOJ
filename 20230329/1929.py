import sys

n, m = map(int, sys.stdin.readline().split())
nums = [True] * (m + 1)  # 먼저 모든 숫자를 소수로 가정하고 True로 초기화합니다.

nums[0] = False  # 0과 1은 소수가 아니므로 False로 설정합니다.
nums[1] = False

for i in range(2, int(m**0.5) + 1):
    if nums[i]:  # i가 소수인 경우
        for j in range(i*i, m + 1, i):  # i의 배수를 모두 소수가 아닌 것으로 표시합니다.
            nums[j] = False

for i in range(n, m + 1):
    if nums[i]:  # 소수인 경우 출력합니다.
        print(i)
