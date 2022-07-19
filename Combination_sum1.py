def possible(lis,target):
    res=[]
    targetsum=[]
    dic={}
    lis.sort()
    def dfs(templis,index,res):
        if index==len(lis):
            res.append(templis)
            if sum([lis[i] for i in range(len(lis)) if templis[i]==1])==target and ','.join([str(lis[i]) for i in range(len(lis)) if templis[i]==1]) not in dic:
                targetsum.append([lis[i] for i in range(len(lis)) if templis[i]==1])
                dic[','.join([str(lis[i]) for i in range(len(lis)) if templis[i]==1])]=1
        else:
            templis1=templis[::]
            templis.append(0)
            templis1.append(1)
            dfs(templis,index+1,res)
            dfs(templis1,index+1,res)
    dfs([],0,res)
    return [targetsum,dic]
def main(args):
    target=2
    lis=[0,1,2,2]
    for line in possible(lis,target):
        print(line)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
