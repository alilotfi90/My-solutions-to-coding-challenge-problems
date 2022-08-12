def uniquePathsWithObstacles(obstacleGrid):
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0 for i in range(n)] for j in range(m)]
        if obstacleGrid[0][0]==1:
            return 0
        dp[0][0]=1
        for i in range(1,m):
            if obstacleGrid[i][0]==0:
                dp[i][0]=dp[i-1][0]
        for j in range(1,n):
            if obstacleGrid[0][j]==0:
                dp[0][j]=dp[0][j-1]
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        print(dp)
        return dp[m-1][n-1]
def main():
    grid_map=[[0,0,0],[0,1,0],[0,0,0]]
    print(uniquePathsWithObstacles(grid_map))
    

if __name__ == "__main__":
  main()