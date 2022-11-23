from typing import List

def minimum_total(triangle: List[List[int]]) -> int:
    m=len(triangle)
    dp=[[] for i in range(m)]
    for row in range(m):
        for j in range(len(triangle[row])):
            dp[row].append(0)
#     print(dp)
    for row in range(m):
        for j in range(len(dp[row])):
            if row==0:
                dp[row][0]=triangle[row][0]
            else:
                if j==0 or j==row:
                    if j==0:
                        dp[row][j]=dp[row-1][j]+triangle[row][j]
                    else:
                        dp[row][j]=dp[row-1][j-1]+triangle[row][j]
                        
                else:
                    dp[row][j]=min(dp[row-1][j],dp[row-1][j-1])+triangle[row][j]
                    
    
    return min(dp[m-1])