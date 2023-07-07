def solution(triangle):
    dp = [triangle[0]]
    for i in range(1,len(triangle)):
        arr = []
        arr.append(dp[i-1][0]+triangle[i][0])
        arr.append(dp[i-1][-1]+triangle[i][-1])
        for j in range(1,len(triangle[i])-1):
            arr.insert(j,max(dp[i-1][j-1], dp[i-1][j])+triangle[i][j])
        dp.append(arr)
    
    return max(arr)