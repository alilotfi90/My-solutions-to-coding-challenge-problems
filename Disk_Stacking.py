
def main():
    matrix=[[2,1,2,3],[3,2,3,4],[2,2,8,4],[2,3,4,2],[1,3,1,2],[4,4,5,5]]
    print(matrix)
    size=2
    m=len(matrix)
    n=len(matrix[0])
    for i in range(m-size):
      for j in range(n-size):
        #print(matrix[i:i+size-1][j])
        continue
    fixi=0
    fixj=0
    size=2
    #print([[matrix[i][j] for j in range(fixi+size)] for i in range(fixj+size)])
    count=0
    for fixi in range(0,m-size+1):
      for fixj in range(0,n-size+1):
        print([[matrix[i][j] for j in range(fixj,fixj+size)] for i in range(fixi,fixi+size)])
        #print('if you wanna go right')
        #print('col to remove')
        #print([matrix[i][fixj] for i in range(fixi,fixi+size)])
        #print('col to add')
        #print([[matrix[i][j] for j in range(fixj,fixj+size)] for i in range(fixi,fixi+size)])
    lis=[[1,2],[2,1]]
    print(sum([sum(lis[i]) for i in range(len(lis))]))
    dp=[[0 for j in range(0,n-size+1)] for i in range(m-size+1)]
    # to calculate dp[0][0]
    fixi=0
    fixj=0
    dp[0][0]=sum([sum([matrix[i][j] for j in range(fixj,fixj+size)]) for i in range(fixi,fixi+size)])
    print(dp)
    for fixj in range(1,n-size+1):
      print([[matrix[i][j] for j in range(fixj,fixj+size)] for i in range(fixi,fixi+size)])
      dp[fixi][fixj]=dp[fixi][fixj-1]+sum([matrix[i][fixj+size-1] for i in range(fixi,fixi+size)])-sum([matrix[i][fixj-1] for i in range(fixi,fixi+size)])
    for fixj in range(0,n-size+1):
      for fixi in range(1,m-size+1):
        dp[fixi][fixj]=dp[fixi-1][fixj]-sum([matrix[fixi-1][j] for j in range(fixj,fixj+size)])+sum([matrix[fixi+size-1][j] for j in range(fixj,fixj+size)])
      

    print(dp)
    lis=[a for b in dp for a in b]
    print(max(lis))
    

if __name__ == "__main__":
  main()