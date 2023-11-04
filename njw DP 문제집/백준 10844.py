N = int(input())

dp = [[0]*10 for _ in range(N+1)]

dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def count_nums(n):
    for i in range(10):
        if i == 0:
            dp[n][i] = dp[n-1][i+1]

        elif i == 9:
            dp[n][i] = dp[n-1][i-1]

        else:
            dp[n][i] = dp[n-1][i-1] + dp[n-1][i+1]


for j in range(2, N+1):
    count_nums(j)

print(dp)

print((sum(dp[N]) - dp[N][0]) % 1000000000)
