from math import sqrt
def perfect_squares(n):
    #dp=[something]*(n+1), something<=100000
    dp=[100000]*(n+1)
    dp[0]=0
    for i in range(1,int(sqrt(n))+1):
        cur=i*i
        for j in range(cur,n+1):
            dp[j]=min(dp[j],1+dp[j-cur])
    return dp[n]
def main():
  print(perfect_squares(5))
  print(perfect_squares(64))    
if __name__ == "__main__":
  main()