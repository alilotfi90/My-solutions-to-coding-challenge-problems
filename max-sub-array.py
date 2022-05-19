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
import math as m
def maxsubcrossing(lis,mid):
	tempsum=float('-inf')
	for low in range(mid+1):
		for high in range(mid+1,len(lis)+1):
			temp=sum(lis[low:high+1])
			if temp>=tempsum:
				tempsum=temp
	return tempsum
def maxsub(lis):
	if len(lis)==0:
		return 0
	elif len(lis)==1:
		return lis[0]
	else:
		mid=len(lis)//2
		return max(maxsub(lis[:mid]),maxsub(lis[mid+1:]),maxsubcrossing(lis,mid))

def main(args):
	lis=[-1,2,3,-1,10]
	mid=len(lis)//2
	print(lis[:mid])
	print(lis[mid+1:])
	print(maxsub(lis))
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
