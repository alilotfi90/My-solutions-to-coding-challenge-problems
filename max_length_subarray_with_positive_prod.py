def getMaxLen(nums):
        n=len(nums)
        pos=[0]*n
        neg=[0]*n
        long=0
        if nums[0]==0:
            pos[0]=0
            neg[0]=0
        elif nums[0]>0:
            pos[0]=1
            neg[0]=0
        else:
            pos[0]=0
            neg[0]=1
        long=pos[0]
        for i in range(1,n):
            if nums[i]==0:
                pos[i]=0
                neg[i]=0
            if nums[i]>0:
                pos[i]=1+pos[i-1]
                if neg[i-1]==0:
                    neg[i]=0
                else:
                    neg[i]=1+neg[i-1]
            if nums[i]<0:
                if neg[i-1]==0:
                    pos[i]=0
                else:
                    pos[i]=1+neg[i-1]
                neg[i]=1+pos[i-1]
            long=max(long,pos[i])
        return long
def main():
    array=[1,2,0,-1,2,-10]
    print(getMaxLen(array))
    

if __name__ == "__main__":
  main()