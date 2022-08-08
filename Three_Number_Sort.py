def threeNumberSort(lis1, lis2):
    count={}
    count[lis2[0]]=0
    count[lis2[1]]=0
    count[lis2[2]]=0
    i=0
    while i<len(lis1):
        if lis1[i]==lis2[0]:
            lis1.insert(count[lis2[0]],lis1[i])
            lis1.pop(i+1)
            count[lis2[0]]+=1
            i+=1
            continue
        if lis1[i]==lis2[1]:
            lis1.insert(count[lis2[0]]+count[lis2[1]],lis1[i])
            lis1.pop(i+1)
            i+=1
            count[lis2[1]]+=1
            continue
        if lis1[i]==lis2[2]:
            lis1.insert(count[lis2[0]]+count[lis2[1]]+count[lis2[2]],lis1[i])
            lis1.pop(i+1)
            i+=1
            count[lis2[2]]+=1
            continue
    return lis1

def main():
    lis1=[1,1,1,-1,-1,0,-1,-1]
    lis2=[1,0,-1]
    print(threeNumberSort(lis1, lis2))
    

if __name__ == "__main__":
  main()