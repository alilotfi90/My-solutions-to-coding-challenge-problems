from collections import deque
class Node:
	def __init__(self,val,left=None,right=None):
		self.val=val
		self.left=left
		self.right=right
def level_order_traversal(root):
    queue=deque([root])
    res=[]
    while len(queue)!=0:
        n=len(queue)# n is the number of not null nodes in the currenr level
        curlevel=[]
        for i in range(n):
            newnode=queue.popleft()
            curlevel.append(newnode.val)
            for child in [newnode.left,newnode.right]:
                if child!=None:
                    queue.append(child)
        res.append(curlevel)
    return res
def main():
    print('Here we build a tree and print according to level')
    root=Node(0)
    root.left=Node(1)
    root.right=Node(2)
    root.left.left=Node(3)
    root.left.right=Node(4)
    root.right.left=Node(5)
    root.right.right=Node(6)
    for line in level_order_traversal(root):
    	print(line)
    
    
if __name__ == "__main__":
  main()