from typing import List

def knapsack_weight_only(lis):
    #lis=[1,3,3,5]
    if len(lis)==1:
        return list(set([0,lis[0]]))
    memo={}
    memo[-1]=set()
    memo[-1].add(0)
    n=len(lis)
    for i in range(0,n):
        memo[i]=set()
        for a in memo[i-1]:
            memo[i].add(a+0)
            memo[i].add(a+lis[i])
    return list(memo[n-1])
def main():
    nums=[125,1,8,3,24,9,18,2,4,25,12,72]
    nums.sort()
    n=len(nums)
    print(nums)
    dp=[0 for i in range(n)]
    dp[n-1]=1
    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            if nums[j]%nums[i]==0 and dp[i]<=dp[j]:
                dp[i]=dp[j]+1
    print(dp)
    print(2%4)

if __name__ == "__main__":
  main()