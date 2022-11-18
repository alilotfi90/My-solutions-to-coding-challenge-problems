def geteven(string,i,j):
    while i>=0 and j<len(string):
        if string[i]!=string[j]:
            break
        i-=1
        j+=1
    return [i+1,j]
def getodd(string,i):
    k=1
    while i-k>=0 and i+k<len(string) and string[i-k]==string[i+k]:
        k+=1
    return [i-k+1,i+k]
def longestPalindromicSubstring(string):
    curbegin=0
    curend=1
    maxpal=[0,1]
    for i in range(1,len(string)):
        even=geteven(string,i-1,i)
        odd=getodd(string,i)
        maxpal=max(odd,even,maxpal,key=lambda x:x[1]-x[0])
    return string[maxpal[0]:maxpal[1]]
string="cababacadcb"
print(longestPalindromicSubstring(string))