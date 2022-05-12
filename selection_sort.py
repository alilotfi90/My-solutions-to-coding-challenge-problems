#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  slow_sort.py
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
import numpy as np
def select_sort(lis):
	lis1=lis
	index_list=range(0,len(lis1)-1)
	
	for i in index_list:
		min_index=i
		for j in range(i,len(lis1)):
			if lis1[j]<lis1[min_index]:
				min_index=j
		if min_index!=i:
			lis1[i] , lis1[min_index] = lis1[min_index] , lis1[i]  
	return lis1
def insertion_sort(lis):  
	lis1=[]
	for i in range(len(lis)):
		lis1.append(lis[i])
		j=i-1
		while j>=0 and lis1[i]<lis1[j]:
			lis1[i] , lis1[j] = lis1[j] , lis1[i]
	return lis1
def change(C,n):
	C.sort()
	return n
def main(args):
	C=[2,5,3,6]
	
	print(change(C,5)) 			 
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
