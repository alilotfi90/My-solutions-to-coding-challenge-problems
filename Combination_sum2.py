def possible(lis,target):
    res=[]
    def dfs(nums,index,remain,path):
        if remain==0:
            res.append(path[:])
        else:
            for i in range(index,len(nums)):
                num=nums[i]
                if remain-num<0:
                    continue
                dfs(nums,i,remain-num,path+[num])
    dfs(lis,0,target,[])
    return res
    return [res,targetsum,dic]
def main(args):
    target=5
    lis=[1,2,4]
    print(possible(lis,target))
    # use dfs, with inputs: 1- lis 2- index of last used element, 3-remaining value 4- path     

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
