def longestCommonSubsequence(str1, str2):
    if len(str1)==0 or len(str2)==0:
        return []
    m=len(str1)+1
    n=len(str2)+1
    dp=[[[] for i in range(n)] for j in range(m)]
    for i in range(n):
        dp[0][i]=[]
    for i in range(m):
        dp[i][0]=[]
    for i in range(1,m):
        for j in range(1,n):
            if str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]+[str1[i-1]]
            else:
                if len(dp[i][j-1])>len(dp[i-1][j]):
                    dp[i][j]=dp[i][j-1]
                else:
                    dp[i][j]=dp[i-1][j]
    return dp[m-1][n-1]