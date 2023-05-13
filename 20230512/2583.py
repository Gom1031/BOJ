# m, n 크기의 모눈종이 k개의 직사각형을 그릴 때
# k개의 직사각형의 내부를 제외한 부분이 몇 개의 분리된 영역
# m, n, k 그리고 k개의 직사각형 좌표가 주어질 때
# 몇 개의 분리된 영역으로 나누어지는지
# 각 영역의 넓이가 얼마인지

import sys

m, n, k = map(int, sys.stdin.readline().split())

for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

graph = [[[0] for _ in range(n)] for _ in range(m)]
visited = []

def bfs():