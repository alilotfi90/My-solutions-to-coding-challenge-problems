def kadanesAlgorithm(array):
    if len(array)==0:
        return 0
    n=len(array)
    dp=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i>j:
                dp[i][j]=-float('inf')
    dp[0][0]=array[0]
    for i in range(1,n):
        dp[0][i]=dp[0][i-1]+array[i]
    for j in range(1,n):
        for i in range(1,j+1):
            dp[i][j]=dp[i-1][j]-array[i-1]
    return dp
def main():
    lis=[-1,-2,-3,-4,-5,-6]
    for line in kadanesAlgorithm(lis):
        print(line)

if __name__ == "__main__":
  main()