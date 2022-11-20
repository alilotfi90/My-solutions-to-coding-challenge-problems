def reverseWordsInString(string):
    string1=string[::-1]
    n=len(string1)
    cur=0
    retstring=""
    tempstring=""
    while cur<n:
        if cur==n-1:
            tempstring=string1[cur]+tempstring
            retstring=retstring+tempstring
            # print(revstring(tempstring))
            break
        if string1[cur]==" ":
            retstring=retstring+tempstring
            retstring=retstring+string1[cur]
            tempstring=""
            cur+=1
        else:
            tempstring=string1[cur]+tempstring
            cur+=1
    return retstring
    