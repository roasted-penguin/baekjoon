N = int(input())
dp = [[0,0],[0,1],[1,0]]

for i in range(3,N+1):
    a = dp[i-1][0] + dp[i-1][1]
    b = dp[i-1][0]
    dp.append([a,b])

print(dp[N][0]+dp[N][1])
