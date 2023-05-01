# 첫번째 원소 뽑기/ 왼쪽으로 하난 이동/ 오른쪽으로 한칸 이동
# 큐에 포함되어있던 수 n이 주어진다.뽑아내려고 하는 원소의 위치
# 해당 원소를 주어진 순서대로 뽑는데 드는 2, 3번 연산의 최솟값

from collections import deque

count = 0

# 큐의 크기 n 뽑고자 하는 수의 개수 m
n, m = map(int, input().split())

# m개의 위치
popNum = deque(map(int, input().split()))

# 1부터 n 까지 deque에 넣기
nums = deque(range(1, n+1))

while popNum:
    # 맨 앞 출력
    if popNum[0] == nums[0]:
        popNum.popleft()
        nums.popleft()
    # 왼쪽순환
    elif nums.index(popNum[0]) <= len(nums) // 2:
        nums.rotate(-1)
        count += 1
    # 오른쪽순환
    else:
        nums.rotate(1)
        count += 1
print(count)