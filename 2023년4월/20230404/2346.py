from collections import deque

n = int(input())
balloons = deque(enumerate(map(int, input().split()), start=1))

result = []

while balloons:
    # 터뜨릴 풍선을 찾고 결과 리스트에 추가합니다.
    index, move = balloons.popleft()
    result.append(index)

    # 풍선이 남아 있다면 다음 풍선의 위치로 이동합니다.
    if balloons:
        if move > 0:
            move -= 1
        balloons.rotate(-move)

print(*result)