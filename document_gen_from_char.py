def generateDocument(characters, document):
    dic={}
    for char in characters:
        if char in dic:
            dic[char]+=1
        else:
            dic[char]=1
    for char in document:
        if char not in dic:
            return False
        else:
            dic[char]-=1
            if dic[char]<0:
                return False
    return True