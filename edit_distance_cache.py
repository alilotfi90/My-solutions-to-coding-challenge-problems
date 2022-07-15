from functools import lru_cache
from math import inf
def min_distance(word1,word2):
    mindist=inf
    lis=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    dic={}
    for i in range(len(lis)):
        dic[lis[i]]=ord(lis[i])-ord('a')
    costs=[0 for i in range(26)]
    costs[0]=1
    costs[1]=2
    costs[2]=3
    for a in dic.keys():
        dic[a]=costs[dic[a]]
    @lru_cache(None)
    def dfs(i,j,dist):
        nonlocal mindist
        if i==len(word1) and j==len(word2):
            mindist=min(dist,mindist)
            return 
        if i==len(word1):
            dist+=len(word2)-j
            for k in range(j+1,len(word2)):
                dist+=dic[word2[k]]

            mindist=min(dist,mindist)
            return
        if j==len(word2):
            for k in range(i+1,len(word1)):
                dist+=dic[word1[k]]
            mindist=min(dist,mindist)
            return
        if word1[i]==word2[j]:
            dfs(i+1,j+1,dist)
        dfs(i+1,j,dist+1)#remove i
        dfs(i,j+1,dist+1)#remove j
        dfs(i+1,j+1,dist+1)#replace one of them
    dfs(0,0,0)
    return mindist
def main():
    word1="abb"
    word2="bba"
    print(min_distance(word1,word2))
    lis=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    dic={}
    for i in range(len(lis)):
        dic[lis[i]]=ord(lis[i])-ord('a')
    costs=[0 for i in range(26)]
    costs[0]=1
    costs[1]=2
    costs[2]=3
    for a in dic.keys():
        dic[a]=costs[dic[a]]
    print(dic)
    print(min_distance(word1,word2))
    
if __name__ == "__main__":
  main()