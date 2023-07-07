def solution(m, n, puddles):
    dp = [[0 for j in range(m+2)] for i in range(n+2)]
    for y in range(1,n+1):
        for x in range(1,m+1):
                if x==1 and y==1:
                    dp[y][x]=1
                elif [x,y] in puddles:
                    dp[y][x] = 0
                else:
                    dp[y][x] = dp[y-1][x] + dp[y][x-1]
    return dp[n][m]%1000000007