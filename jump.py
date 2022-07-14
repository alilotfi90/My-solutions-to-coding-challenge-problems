def canJump(nums):
    n=len(nums)
    if n==1:
        return True
    dp=[False for i in range(n)]
    dp[n-1]=True
    prevgood=n-1
    minreq=0
    for i in range(n-2,-1,-1):
        if prevgood-i<=nums[i]:
            dp[i]=True
            prevgood=i
    return dp[0]
def main():
    lis=[2,1,0,3,4]
    print(canJump(lis))
if __name__ == "__main__":
  main()
