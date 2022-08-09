def festival_game(target):
    dp=[[0]*len(target) for _ in range(len(target))]
    def dfs(l,r):
        if dp[l][r]!=0:
            return dp[l][r]
        # Assume we start analyzing interval [l,r], and hit i last, then left-most and right-most unhit target are:
        # target[l-1] and target[r+1] assuming they exist, otherwise 1
        for i in range(l,r+1):
            leftval=0 if i==l else dfs(l,i-1)
            rightval=0 if i==r else dfs(i+1,r)
            val= (1 if l==0 else target[l-1])* target[i] * (1 if r==len(target)-1 else target[r+1])
            dp[l][r]=max(dp[l][r],leftval+val+rightval)
        
        return dp[l][r]
    return dfs(0,len(target)-1)
def main():
    target=[1,5,4]
    print(festival_game(target))
    

if __name__ == "__main__":
  main()