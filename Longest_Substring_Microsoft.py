def longestValidString(string):
    n=len(string)
    dp=[[False for i in range(n)] for j in range(n)]
    for k in range(0,n):
        for i in range(0,n-k):
            j=i+k
            if k<=2:
                dp[i][j]=True
            else:
                if dp[i][j-1]==True:
                    if string[j-1]!=string[j-2] or string[j-2]!=string[j-3]:
                        dp[i][j]=True
                    else:
                        dp[i][j]=False

    maxval=0
    maxi=0
    maxj=0
    for i in range(n):
        for j in range(i,n):
            if dp[i][j]==True and maxval<j-i:
                maxval=j-i
                maxj=j
                maxi=i
    return string[maxi:maxj]
def main():
    string="abbbbbbbacvfd"
    print(longestValidString(string))
if __name__ == "__main__":
  main()