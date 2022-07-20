def possible(lis,target):
    res=[]
    targetsum=[]
    dic={}
    lis.sort()
    def dfs(templis,index,res):
        if index==len(lis):
            res.append(templis)
            if sum([lis[i] for i in range(len(lis)) if templis[i]!=0])==target and ','.join([str(lis[i]) for i in range(len(lis)) if templis[i]!=0]) not in dic:
                targetsum.append([lis[i] for i in range(len(lis)) if templis[i]!=0])
                dic[','.join([str(lis[i]) for i in range(len(lis)) if templis[i]!=0])]=1
        else:
            if lis[index]!=0:
                k=target//lis[index]
                genlis=[[] for j in range(k+1)]
                for i in range(k+1):
                    genlis[i]=templis[::]
                    genlis[i].append(i)
                    dfs(genlis[i],index+1,res)


    dfs([],0,res)
    return [res,targetsum,dic]
def main(args):
    target=5
    lis=[1,2,4]
    print(possible(lis,target)[1])
        

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
