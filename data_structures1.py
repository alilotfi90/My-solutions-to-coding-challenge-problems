#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  data_structures1.py
#  
#  Copyright 2021 Ali Lotfi <ali@ali-Oryx-Pro>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.s
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import random
from collections import deque
class Vertex:
	def __init__(self,n):
		self.name=n
		self.neighbors=set()
	def add_neighbor(self,v):
		self.neighbors.add(v)
class Graph:
	def __init__(self):
		self.vertices={}
	
	def add_vertex(self,vertex):
		if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name]=vertex
			return True
		else:
			return False
	def add_edge(self,u,v):
		if u in self.vertices and v in self.vertices:
			self.vertices[u].add_neighbor(v)
			self.vertices[v].add_neighbor(u)
			return True
		else:
			return False
	def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key,sorted(list(vertices[key].neighbors)))
class Tree:
	def __init__(self,data,left=None,right=None):
		self.data=data
		self.left=left
		self.right=right
	def insert(self,data):
		if self.data==data:
			return False
		elif self.data>data:
			if self.left is not None:
				return self.left.insert(data)
			else:
				self.left=Tree(data)
				return True
		else:
			if self.right is not None:
				return self.right.insert(data)
			else:
				self.right=Tree(data)
				return True
	def find(self,data):
		if self.data==data:
			return data
		elif data < self.data:
			if self.left is None:
				return False
			else:
				return self.left.find(data)
		elif self.data < data:
			if self.right is None:
				return False
			else:
				return self.right.find(data)

class Node:
	def __init__(self,d,n=None,p=None):
		self.data=d
		self.next=n
		self.previous=p
class Linkedlist:
	def __init__(self,r=None):
		self.root=r
		self.size=0
	def add(self,d):
		new_node=Node(d,self.root)
		self.root=new_node
		self.size+=1
	def find(self,d):
		this_node=self.root
		while this_node is not None:
			if this_node.data==d:
				return d
			else:
				this_node=this_node.next
	def remove(self,d):
		this_node=self.rootnode
		prev_node=None
		while this_node is not None:
			if this_node.data==d:
				if prev_node is not None:
					prev_node.next=this_node.next
				else:
					self.root=this_node.next
				self.size-=1
				return True
			else:
				prev_node=this_node
				this_node=this_node.next
		return False
	def print_list(self):
		this_node=self.root
		while this_node is not None:
			print(this_node.data)
			this_node=this_node.next
class MaxHeap:
	def __init__(self,items=[]):
		self.heap=[0]
		for item in items:
			self.heap.append(item)
			self.__floatUp(len(self.heap)-1)
	def push(self,data):
		self.heap.append(data)
		self.__floatUp(len(self.heap)-1)
	def peek(self):
		if self.heap[1]:
			return self.heap[1]
		else:
			return False
	def pop(self):
		if len(self.heap)>2:
			self.__swap(1,len(self.heap)-1)
			max=self.heap.pop()
			self.__bubbleDown(1)
		elif len(self.heap)==2:
			max=self.heap.pop()
		else:
			max=False
		return max
	def __swap(self,i,j):
		self.heap[i] , self.heap[j] = self.heap[j] , self.heap[i]
	def __floatUp(self,index):
		parent=index//2
		if index<=1:
			return
		elif self.heap[index]>self.heap[parent]:
			self.__swap(index,parent)
			self.__floatUp(parent)
	def __bubbleDown(self,index):
		left=index*2
		right=index*2+1
		largest=index
		if len(self.heap)>left and self.heap[largest]<self.heap[left]:
			largest=left
		if len(self.heap)>right and self.heap[largest]<self.heap[right]:
			largest=right
		if largest!=index:
			self.__swap(index,largest)
			self.__bubbleDown(largest)
	def __str__(self):
		return str(self.heap)
class Stack():
	def __init__(self):
		self.stack=list()
	def push(self,item):
		self.stack.append(item)
	def pop(self):
		if len(self.stack)>0:
			return self.stack.pop()
		else:
			return None
	def peek(self):
		if len(self.stack)>0:
			return self.stack[len(self.stack)-1]
		else:
			return None
	def __str__(self):
		return str(self.stack)

class Graph:
	def __init__(self,graph):
		self.vertex=graph.keys()
		self.edges=graph.values()
class BinaryTreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    
    # below data members used only for some of the problems
    self.next = None
    self.parent = None
    self.count = None
class node():
	def __init__(self, data, nex):
		self.data=data
		self.nex=nex
import numpy as np
class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None
def isSafe(i, j, board):
  for c in range(len(board)):
    for r in range(len(board)):
      if board[c][r] == 'q' and i==c and j!=r:
        return False
      elif board[c][r] == 'q' and j==r and i!=c:
        return False
      elif (i+j == c+r or i-j == c-r) and board[c][r] == 'q':
        return False
  return True 


def main(args):
	x=BinaryTreeNode(3)
	print(x.data)
	print(x.left)
	print("here")
	n = 4
	board = [["-" for _ in range(n)] for _ in range(n)]
	print(board)
	board=["-q--","---q","q---","--q-"]
	print(len(board))
	if len(board)==1:
		return 'q'
	else:
		subboard=[]
		for i in range(len(board)-1):
			subboard.append(board[i][0:len(board[i])-1])
		print(subboard)
	string=["put-between"]
	if string[0][3]=='-':
		print(string)
		print(string[0])
		print(string[0][0:3]+'X'+string[0][4:len(string[0])])
		string1=string[0][0:3]+'X'+string[0][4:len(string[0])]
		print(string1)
		print('starts here')
		lis=[1,2,3,5,6,7]
		lis1=[5,6]
		lis.pop()
		lis.insert(0,10)
		print(lis)
		lis.append(2)
		print(lis)
	x=[1,2,3]
	a,b,c=x
	x=int()
	print(x+1)
	x=[1,2,-2,4,5,6]
	y=sorted(x)
	print(x)
	print(y)
	a=(1,2)
	set1={1,2,3}
	set2={2,3,4}
	print(set2 <= set1)
	lis=[1,2,'b',1,'a','*']
	lis.sort()
	print(lis)
	dic={'d':4,'a':1,'b':2,'c':3}
	lis=list(dic)
	print()
	string=' hello stri '
	print(string.strip())
	print(string)
	lis=[1,2,3,4]
	lis.pop(0)
	lis.insert(0,1)
	print(lis)
	x=3
	print(dic)
	del(dic['a'])
	print(dic)
	print(len(dic))
	print(dic.keys())
	print(dic.values())
	print(type(dic.items()))
	a=['a1','a2','a3']
	b=[c for c in enumerate(a)]
	dic={'A':['B','C'],'B':['C'],'C':[]}
	G=Graph(dic)
	print(G.vertex)
	print(G.edges)
	deq=deque()
	deq.appendleft(2)
	print(deq)
	deq.append(3)
	deq.appendleft(4)
	print(deq)
	names=['cosm','Pedro','Anu','Ray']
	idx=[k for k, v in enumerate(names) if v=='Anu']
	print(idx)
	letters=[x for x in 'ABCDEF']
	print(letters)
	random.shuffle(letters)
	print(letters)
	print([a for a in letters if a!='C'])
	#Here we willl talk about stacks
	lis=list()
	lis.append(1)
	lis.append(2)
	
	lis=Stack()
	lis.push(2)
	lis.push(3)
	lis.peek()
	my_queue=deque()
	my_queue.append(5)
	my_queue.append(5)
	my_queue.appendleft(6)
	my_queue.popleft()
	
	print(my_queue)
	a=[1,2,3]
	print(max(a))
	
	m=MaxHeap([95,3,21])
	print(m)
	m.push(96)
	print(m)
	m.pop()
	print(m)
	print(m.peek())
	l=Node()
	l.data=0
	print(l.data)
	print(l)
	ll=Linkedlist(l)
	lsec=Node(2)
	lsec.data=3
	print(lsec.data)
	print(ll.print_list)
	g=Graph
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
