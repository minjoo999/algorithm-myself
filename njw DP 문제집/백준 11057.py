N = int(input())

# n자리 수일 때 오르막수의 갯수

dp = [[0]*10 for _ in range(N+1)]

dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# dp[2][0] = dp[1][0] + dp[1][1] + ... + dp[1][9]
# dp[2][1] = dp[1][1] + dp[1][2] + ... + dp[1][9]
# 해당 예시처럼 dp[i][j]는 sum(dp[i-1])에서 dp[i-1][0] ~ dp[i-1][j-1] 까지 전부 뺀 값


def count_hill_nums(n):
    sum_dp = sum(dp[n-1])
    res = sum_dp
    dp[n][0] = sum_dp

    for i in range(1, 10):
        res -= dp[n-1][i-1]
        dp[n][i] = res


for j in range(2, N+1):
    count_hill_nums(j)

print(dp)

print(sum(dp[N]) % 10007)
