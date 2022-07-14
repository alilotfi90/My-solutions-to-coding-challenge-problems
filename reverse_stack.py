import stack as s
 
def insertAtBottom(stack, item) :
    if s.isEmpty(stack):
        s.push(stack,item)
    else:
        temp=s.pop(stack)
        insertAtBottom(stack,item)
        s.push(stack,temp)
def reverse(stack):
    if not s.isEmpty(stack):
        temp=s.pop(stack)
        reverse(stack)
        insertAtBottom(stack,temp)
def main():
    stack=s.createStack()
    s.push(stack,1)
    s.push(stack,2)
    s.push(stack,3)
    s.push(stack,4)
    insertAtBottom(stack,5)
    s.printStack(stack)
    reverse(stack)
    print('\n')
    s.printStack(stack)
if __name__ == "__main__":
  main()