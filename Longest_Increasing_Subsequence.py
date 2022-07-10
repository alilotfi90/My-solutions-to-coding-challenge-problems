def main():
    lis=[1,2,3,2,1]
    n=len(lis)
    dp=[1 for i in range(n)]
    nextind=[i for i in range(n)]
    dp[n-1]=1
    for i in range(n-2,-1,-1):
        for j in range(i,n):
            if lis[i]<lis[j]:
                if dp[i]<1+dp[j]:
                    dp[i]=1+dp[j]
                    nextind[i]=j
    print(dp)
    print(nextind)
    maxind=0
    maxval=-float('inf')
    for i in range(n):
        if maxval<dp[i]:
            maxval=dp[i]
            maxind=i
    print(maxval)
    tempind=maxind
    retlis=[]
    while tempind<nextind[tempind]:
        retlis.append(lis[tempind])
        tempind=nextind[tempind]
    retlis.append(lis[tempind])
    print(retlis) 
if __name__ == "__main__":
  main()