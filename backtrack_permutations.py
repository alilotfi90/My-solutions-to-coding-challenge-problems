
def addpath(path,checked,res):
        if len(path)==len(checked):
            res.append(path)
            return
        for i in range(len(checked)):
            if checked[i]:
                continue
            path.append(i)
            checked[i]=True
            addpath(path,checked,res)
            path.pop()
            checked[i]=False
def orig(lis):
    checked=[False for i in range(len(lis))]
    res=[]
    addpath([],[False]*len(lis),res)
    return res


def main():
    result=[]
    origlist=[0,1,2]
    result=orig(origlist)
    print(result)

if __name__ == "__main__":
  main()