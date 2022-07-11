def addpath1(n,checked,res):
        if len(checked)==n:
            lis=[i for i in range(n) if checked[i]==1]
            res.append(lis[:])
            return
        checked.append(0)
        addpath1(n,checked,res)
        checked.pop()
        checked.append(1)
        addpath1(n,checked,res)
        checked.pop()
def orig1(lis):
    checked=[]
    res=[]
    n=len(lis)
    addpath1(n,[],res)
    return res

def main():
    result=[]
    origlist=[0,1,2]
    result1=orig1(origlist)
    print(result1)
    print(len(result1))

if __name__ == "__main__":
  main()