class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    cur1=linkedListOne
    l1=0
    while cur1 is not None:
        l1+=1
        cur1=cur1.next
    print(l1)
    cur2=linkedListTwo
    l2=0
    while cur2 is not None:
        l2+=1
        cur2=cur2.next
    print(l2)
    if l1-l2>=0:
        cur1=linkedListOne
        count=0
        i1=0
        i2=0
        while count<l1-l2:
            cur1=cur1.next
            count+=1
        cur2=linkedListTwo
        while cur1 is not None:
            if cur1==cur2:
                return cur1
            cur1=cur1.next
            cur2=cur2.next
        return None
            
    else:
        cur2=linkedListTwo
        count=0
        i1=0
        i2=0
        while count<l2-l1:
            cur2=cur2.next
            count+=1
        cur1=linkedListOne
        while cur2 is not None:
            if cur1==cur2:
                return cur1
            cur1=cur1.next
            cur2=cur2.next
        return None