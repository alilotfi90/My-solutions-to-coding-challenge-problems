def groupAnagrams(words):
    dic={}
    for word in words:
        st=''.join(sorted(word))
        if st in dic:
            dic[st].append(word)
        else:
            dic[st]=[word]
    retlis=[]
    for key in dic:
        retlis.append(dic[key])
    return retlis