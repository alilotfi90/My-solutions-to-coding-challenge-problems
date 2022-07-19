def minimumTotal(triangle):
        n=len(triangle)
        dp=dp=[[0 for i in range(j+1)] for j in range(n)]
        dp[0][0]=triangle[0][0]
        for i in range(1,n):
            for j in range(i+1):
                if j==0:
                    dp[i][j]=dp[i-1][j]+triangle[i][j]
                    continue
                elif j==i:
                    dp[i][j]=dp[i-1][j-1]+triangle[i][j]
                    continue
                else:
                    dp[i][j]=min(dp[i-1][j-1]+triangle[i][j],dp[i-1][j]+triangle[i][j])
                    continue
        return min(dp[n-1])
def main(args):
    triangle=[[1],[2,4],[3,4,5]]
    print(minimumTotal(triangle))
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
