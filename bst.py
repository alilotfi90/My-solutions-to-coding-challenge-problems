#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  graph.py
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
import numpy as np
def bst(lis,m):
	if len(lis)==0:
		return None
	else:
		left , right = 0 , len(lis)-1
		while left <=right:
			mid=(left+right)//2
			if lis[mid]==m:
				return mid
			if lis[mid]>m:
				right=mid-1
			if lis[mid]<m:
				left=mid+1
		return mid

def main(args):
	lis=[6,5,4,3,2,1]
	print(bst(lis,3))	
		
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
