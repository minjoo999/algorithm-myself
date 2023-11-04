# dp를 통해
# 코드 참고 (출처: https://cotak.tistory.com/12)

N = int(input())

# dp[i][j] : i자리수의 값이 j로 찍히는 경우의 수
dp = [[0]*10 for _ in range(N+1)]

# 모든 자릿수 중 경우의수 초기화 (일단 한번은 나온다고 생각)
# 초기화 방향: 1의 자릿수가 1 ~ 10 인 경우 전부 찍어두기
for i in range(1, 10):
    dp[1][i] = 1

MOD = 1000000000

# 나머지 자릿수 탐색
for i in range(2, N+1):
    for j in range(10):

        # j = 0 -> 그전 자릿수가 1인 경우로 마킹하기
        if j == 0:
            dp[i][j] = dp[i-1][1]

        # j = 9 -> 그전 자릿수가 8인 경우로 마킹하기
        elif j == 9:
            dp[i][j] = dp[i-1][8]

        # 그외: 그전 자릿수에 -1을 한 경우와 +1을 한 경우 모두 찍어두기
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N]) % MOD)
