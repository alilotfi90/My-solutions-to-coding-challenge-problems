import functools
def combinationSum5(nums,target):
    memo={}
    memo[0]=1
    def combs(remain,memo):
        if remain in memo:
            return memo[remain]

        result = 0
        for num in nums:
            if remain - num >= 0:
                result += combs(remain - num,memo)
            
        memo[remain]=result
        return result

    return combs(target,memo)
def main():
  target=4
  nums=[1,3,4,5]
  print(combinationSum5(nums,target))
  #dic={}
  #dic[1]=0
  #dic[0]=0
  #dic[2]=0
  #lis=dic.keys()
  #lis=sorted(lis)
  #dic=dict({1:0,2:0,3:0})
  #print(dic)
    

if __name__ == "__main__":
  main()