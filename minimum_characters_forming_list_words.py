def minimumCharactersForWords(words):
    dic={}
    for word in words:
        # form temp dic
        # as you form temp dic, compare it to the main dic and update main dic if needed
        tempdic={}
        for char in word:
            if char in dic:
                if char not in tempdic:
                    tempdic[char]=1
                else:
                    tempdic[char]+=1
                    if tempdic[char]>dic[char]:
                        dic[char]=tempdic[char]
            else:
                dic[char]=1
                if char in tempdic:
                    tempdic[char]+=1
                    dic[char]=tempdic[char]
                else:
                    tempdic[char]=1
        
    retlis=[]
    for char in dic:
        for i in range(dic[char]):
            retlis.append(char)
    return retlis