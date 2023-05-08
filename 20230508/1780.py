# n*n 크기의 종이
# -1, 0, 1 중 하나가 저장 / 적절한 크기로 자르기
# >종이가 모두 같은수라면 그대로 사용
# >모두같은수가아니라면 같은크기 9개로 자르고 반복
# -1, 0, 1로만 채워진 종이의 개수는?

import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(graph)