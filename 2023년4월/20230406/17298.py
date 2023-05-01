import sys

# 수열 크기 n
n = int(sys.stdin.readline())

# 숫자들
nums = list(map(int, sys.stdin.readline().split()))

stack = []
result = [-1] * n


for i in range(n):
    while stack and nums[stack[-1]] < nums[i]:
        idx = stack.pop()
        result[idx] = nums[i]
    stack.append(i)

print(*result)


# for _ in range(n-1):
#     compare = nums.pop(0)
#     for i in nums:
#         if compare >= i:
#             continue
#         elif compare < i:
#             result.append(i)
#             break
#     else:
#         result.append(-1)
# result.append(-1)
# print(*result)