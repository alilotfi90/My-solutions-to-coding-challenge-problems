def maxProduct(nums):
        n=len(nums)
        min_so_far=[0]*n
        max_so_far=[0]*n
        min_so_far[0] , max_so_far[0] , result = nums[0] , nums[0] , nums[0]
        for i in range(1,n):
            max_so_far[i]=max(nums[i],nums[i]*min_so_far[i-1],nums[i]*max_so_far[i-1])
            min_so_far[i]=min(nums[i],nums[i]*min_so_far[i-1],nums[i]*max_so_far[i-1])
            result=max(result,max_so_far[i])
        return result
def main():
    array=[1,2,0,-1,2,-10]
    print(maxProduct(array))
    

if __name__ == "__main__":
  main()