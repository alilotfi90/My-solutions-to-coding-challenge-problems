class LinkedList:
	def __init__(self,value):
		self.value=value
		self.next= None
	def printlist(self):
		inroot=self
		root=self
		while root is not None:
			print(root.value,"-->",end=" ")
			root=root.next
			if root==inroot:
				return
		print()
	def makellfromlist(self,lis):
		for i in range(0,len(lis)):
			if i==0:
				cur=LinkedList(lis[i])
				self.next=cur
			else:
				temp=LinkedList(lis[i])
				cur.next=temp
				cur=temp
def node_next(node):
	return node.next or node
def detect_cycle(node):
	turt=node_next(node)
	rab=node_next(node_next(node))
	while turt!=rab and rab.next is not None:
		turt=node_next(turt)
		rab=node_next(node_next(rab))
	return rab.next is not None
def main(args): 
	h0=LinkedList(0)
	#h1.makellfromlist([6,7,8])
	le=10
	lis=[0 for i in range(10)]
	lis[0]=h0
	for i in range(1,le):
		lis[i]=LinkedList(i)
		if i==1:
			h0.next=lis[i]
		else:
			lis[i-1].next=lis[i]

	lis[9].next=lis[0]
	#print(lis[9].next.value)
	lis[0].printlist()
	print('\n hi')
	print(node_next(lis[9]).value)
	print(detect_cycle(lis[8]))
''
if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
