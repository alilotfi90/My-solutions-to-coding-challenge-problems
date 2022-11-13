def sortStack(stack):
    if len(stack)<=1:
        return stack
    a=stack.pop()
    sortStack(stack)
    if stack[-1]<=a:
        stack.append(a)
        return stack
    else:
        b=stack.pop()
        stack.append(a)
        sortStack(stack)
        stack.append(b)
        return stack