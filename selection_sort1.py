def main():
    lis=[2,3,1,-1,2]
    n=len(lis)
    sortlis=[]
    startind=0
    while startind<n:
        toadd=lis[startind]
        tochangeind=startind
        for i in range(startind+1,n):
            if lis[i]<toadd:
                toadd=lis[i]
                tochangeind=i
        lis[startind] , lis[tochangeind] = lis[tochangeind] , lis[startind]
        startind+=1
    print(lis)

if __name__ == "__main__":
  main()