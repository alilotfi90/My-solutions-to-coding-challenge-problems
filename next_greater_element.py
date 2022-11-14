def nextGreaterElement(array):
    n=len(array)
    if n==0:
        return []
    result=[0]*n
    stack=[]
    maxel=max(array)
    found={}
    for i in range(n):
        if array[i]==maxel:
            found[i]=1
            result[i]=-1
    for i in range(n):
        if len(stack)==0:
            stack.append(i)
            continue
        else:
            while len(stack)!=0 and array[stack[-1]]<array[i]:
                a=stack.pop()
                result[a]=array[i]
                found[a]=1
            if i not in found:
                stack.append(i)
    if len(found)==n:
        return result
    for i in range(n):
        if len(found)==n:
            return result
        while len(stack)!=0 and array[stack[-1]]<array[i]:
            a=stack.pop()
            result[a]=array[i]
            found[a]=1
    return result