n = int(input())
square_num_li = [i*i for i in range(1, 316)]
dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if i in square_num_li:
        dp[i] = 1
    else:
        dp[i] = min([dp[i-j] for j in square_num_li if i-j > 0])+1
print(dp[n])