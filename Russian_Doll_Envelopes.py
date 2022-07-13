def max_layers(envelopes):
    lis=envelopes
    lis.sort(key=lambda x:x[0]+x[1])
    n=len(lis)
    if n==0:
        return 0
    dp=[1 for i in range(n)]
    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            if lis[i][0]<lis[j][0] and lis[i][1]<lis[j][1]:
                dp[i]=max(dp[i],1+dp[j])
    
    return max(dp)
def main():
    lis=[[1,2],[2,3],[1,2],[4,5]]
    print(max_layers(lis))
if __name__ == "__main__":
  main()