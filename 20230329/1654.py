import sys
nums = []
n, m = map(int, sys.stdin.readline().split())

for i in range(n):
    nums.append(int(sys.stdin.readline().rstrip()))

start, end = 1, max(nums)

while start <= end:
    mid = (start + end) // 2  # 중간점 계산
    count = 0  # 현재 길이로 자른 랜선의 개수

    # 자른 랜선의 개수 계산
    for i in nums:
        count += i // mid

    # 개수에 따라 이분 탐색 범위 조절
    if count >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)  # 끝점이 최대 길이