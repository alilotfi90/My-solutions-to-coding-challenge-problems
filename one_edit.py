def oneEdit(stringOne, stringTwo):
    if abs(len(stringOne)-len(stringTwo))>=2:
        return False
    if stringOne==stringTwo:
        return True
    if len(stringOne)==len(stringTwo):
        count=0
        char1=set()
        char2=set()
        for i in range(len(stringOne)):
            if stringOne[i]!=stringTwo[i]:
                count+=1
                char1.add(stringOne[i])
                char2.add(stringTwo[i])
            if count>=2 and char1!=char2:
                return False
        return True
    if len(stringOne)==len(stringTwo)+1 or len(stringOne)+1==len(stringTwo):
        if len(stringOne)+1==len(stringTwo):
            stringOne , stringTwo = stringTwo , stringOne 
        oneind=0
        twoind=0
        n=len(stringTwo)
        count=0
        #st1 abc
        #st2 ac
        while twoind<n:
            if stringOne[oneind]!=stringTwo[twoind]:
                count+=1
                oneind+=1
            else:
                twoind+=1
                oneind+=1
            if count>1:
                return False
        return True