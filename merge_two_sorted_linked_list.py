#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  linked_list_1.py
#  
#  Copyright 2022 Ali Lotfi <ali@ali-Oryx-Pro>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
#class LinkedList:
#    def __init__(self, value):
#        self.value = value
#       self.next = None
#
class LinkedList:
    def __init__(self,value):
    	self.val=value
    	self.next= None
def printlist(head):
    while head is not None:
    	print(head.value)
    	head=head.next
def mergeTwoLists(list1, list2):
        # create a dummy node
        dummy=ListNode(0)
        tail=dummy
        while list1 is not None or list2 is not None:
            if list1==None:
                tail.next=list2
                break
            if list2==None:
                tail.next=list1
                break
            if list1.val<list2.val:
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next
        return dummy.next
def main(args):
	print('merge two LinkedList')

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
