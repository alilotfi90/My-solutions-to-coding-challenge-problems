from typing import Counter
def bigger(check,dic):
    for a in check:
        if a not in dic:
            return False
        if check[a]>dic[a]:
            return False
    return True
def smallestSubstringContaining(bigString, smallString):
    check=Counter(smallString)
    bigdic=Counter(bigString)
    for a in check:
        if a not in bigdic:
            return ""
        if bigdic[a]<check[a]:
            return ""
    minstr=bigString
    dic={}
    left=0
    right=0
    n=len(bigString)
    while right<n:
        print(bigString[left:right])
        if bigString[right] not in check:
            right+=1
            continue
        
        if bigString[right] in dic:
            dic[bigString[right]]+=1
        else:
            dic[bigString[right]]=1
            
        # print(dic)
        while bigger(check,dic) and left<=right:
            if len(bigString[left:right+1])<len(minstr):
                minstr=bigString[left:right+1]
            if bigString[left] not in check:
                left+=1
                continue
            dic[bigString[left]]-=1
            left+=1
            # if len(bigString[left:right+1])<len(minstr):
            #     minstr=bigString[left:right+1]
        right+=1
    return minstr