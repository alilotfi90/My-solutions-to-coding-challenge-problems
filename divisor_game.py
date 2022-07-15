def divisor_game(n):
    if n==1:
        return False
    dp={}
    dp[1]=False
    for i in range(2,n+1):
        dp[i]=False
        for x in range(i-1,0,-1):
            if i%x==0 and dp[i-x]==False:
                dp[i]=True
    return dp[n]
def main():
  n=100
  print(divisor_game(3))
if __name__ == "__main__":
  main()