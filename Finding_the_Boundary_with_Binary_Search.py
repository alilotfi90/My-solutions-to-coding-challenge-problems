#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Finding_the_Boundary_with_Binary_Search.py
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
def fbs(arr):
	left , right = 0 , len(arr)-1
	bindex=-1
	while left<=right:
		mid=(left+right)//2
		if arr[mid]:
			right=mid-1
			bindex=mid
		else:
			left=mid+1
	return bindex
def main(args):
    print("hello")
    lis=[False,False,False,False,False,False, True, True]
    print(fbs(lis))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
