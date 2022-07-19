def numberOfWaysToTraverseGraph(width, height):
    m=height
    n=width
    dp=[[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        dp[0][i]=1
    for j in range(m):
        dp[j][0]=1
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j]=dp[i][j-1]+dp[i-1][j]
    return dp[m-1][n-1]
def main():
    height=40
    width=20
    print(numberOfWaysToTraverseGraph(width, height))
if __name__ == "__main__":
  main()