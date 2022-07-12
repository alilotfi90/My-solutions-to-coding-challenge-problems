def find_largest_subset(nums):
    nums.sort()
    if len(nums)==0:
        return 0
    n=len(nums)
    dp=[1 for i in range(n)]
    #dp[n-1]=1
    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            if nums[j]%nums[i]==0:
                dp[i]=max(dp[i],dp[j]+1)
    return max(dp)
def main():
    nums=[125,1,8,3,24,9,18,2,4,25,12,72]
    print(find_largest_subset(nums))

if __name__ == "__main__":
  main()