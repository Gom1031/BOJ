import sys

def min_clear_time(N, M, weapon_times):
    dp = [[10001] * M for _ in range(N)]

    for j in range(M):
        dp[0][j] = weapon_times[0][j]

    for i in range(1, N):
        for j in range(M):
            for k in range(M):
                if j != k:
                    dp[i][j] = min(dp[i][j], weapon_times[i][j] + dp[i - 1][k])

    return min(dp[-1])

N, M = map(int, sys.stdin.readline().split())
weapon_times = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(min_clear_time(N, M, weapon_times))
