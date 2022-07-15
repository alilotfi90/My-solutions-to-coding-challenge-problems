def maxSumIncreasingSubsequence(array):
    n=len(array)
    if n==0:
        return 0
    dp=[array[i] for i in range(n)]
    nextind=[i for i in range(n)]
    dp[n-1]=array[n-1]
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            if array[i]<array[j] and dp[i]<array[i]+dp[j]:
                dp[i]=array[i]+dp[j]
                nextind[i]=j
    maxval=-float('inf')
    startind=-1
    for i in range(n):
        if dp[i]>maxval:
            maxval=dp[i]
            startind=i
    retlis=[maxval,[]]
    trav=startind
    while nextind[trav]!=trav:
        retlis[1].append(array[trav])
        trav=nextind[trav]
    retlis[1].append(array[trav])
    return retlis
def main():
    arr=[1,-1,-2,2,3]
    print(maxSumIncreasingSubsequence(arr))
    
if __name__ == "__main__":
  main()