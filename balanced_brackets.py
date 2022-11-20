def balancedBrackets(string):
    stack=[]
    for i in range(len(string)):
        if string[i]=="(" or string[i]=="[" or string[i]=="{":
            stack.append(string[i])
        else:
            if string[i]==")":
                if len(stack)==0:
                    return False
                else:
                    if stack[-1]=="(":
                        stack.pop()
                        continue
                    else:
                        return False
                continue
            if string[i]=="]":
                if len(stack)==0:
                    return False
                else:
                    if stack[-1]=="[":
                        stack.pop()
                        continue
                    else:
                        return False
                continue
            if string[i]=="}":
                if len(stack)==0:
                    return False
                else:
                    if stack[-1]=="{":
                        stack.pop()
                        continue
                    else:
                        return False
                continue
    if len(stack)==0:
        return True
    else:
        return False