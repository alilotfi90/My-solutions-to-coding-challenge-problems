class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        print(nums)
        m=len(queries)
        answer=[0]*m
        for i in range(m):
            ind=0
            sum=0
            while sum < queries[i] and ind<len(nums):
                if sum+nums[ind]<=queries[i]:
                    sum+=nums[ind]
                    ind+=1
                else:
                    break
            if ind>0:
                answer[i]=ind
            else:
                answer[i]=0
        return answer