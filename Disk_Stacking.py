def diskStacking(disks):
    disks=sorted(disks,key=lambda x:x[2])
    n=len(disks)
    # dp stores max height possible if disks[i] is a the base
    dp=[disks[i][2] for i in range(n)]
    nextdisk=[i for i in range(n)]
    print(dp)
    for i in range(1,n):
      # fix disks[i]
      for j in range(0,i):
        if disks[i][0] > disks[j][0] and disks[i][1] > disks[j][1] and disks[i][2] > disks[j][2]:
          if dp[i]<disks[i][2]+dp[j]:
            dp[i]=disks[i][2]+dp[j]
            nextdisk[i]=j
    maxind=0
    maximumval=0
    result=[]
    for i in range(n):
      if dp[i]>maximumval:
        maximumval=dp[i]
        maxind=i
    print(dp)
    print(maximumval)
    tempind=maxind
    while nextdisk[tempind]<tempind:
      result.append(disks[tempind])
      tempind=nextdisk[tempind]
    result.append(disks[tempind])
    return result[::-1]
def main():
    disks=[[2,1,2],[3,2,3],[2,2,8],[2,3,4],[1,3,1],[4,4,5]]
    print(diskStacking(disks))
    

if __name__ == "__main__":
  main()