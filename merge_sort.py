#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  merge_sort.py
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

def mergetwosorted(lis1,lis2):
	retlis=[]
	while len(lis1)!=0 or len(lis2)!=0:
		if len(lis1)==0:
			a=lis2.pop()
			retlis=[a]+retlis
			continue
		if len(lis2)==0:
			a=lis1.pop()
			retlis=[a]+retlis
			continue
		if len(lis1)!=0 and len(lis2)!=0:
			if lis1[-1]<=lis2[-1]:
				a=lis2.pop()
				retlis=[a]+retlis
				continue
			else:
				a=lis1.pop()
				retlis=[a]+retlis
				continue
	return retlis
def mergeorted(lis):
	if len(lis)==0:
		return []
	if len(lis)==1:
		return lis
	begin , end = 0 , len(lis)
	mid=(begin+end)//2
	return mergetwosorted(mergeorted(lis[begin:mid]),mergeorted(lis[mid:end]))
def main(args):
    lis=[1,2,3,4,5]
    begin , end = 0 , len(lis)
    mid=(begin+end)//2
    print(lis[begin:mid])
    print(lis[mid:end])
    lis1=[1,3,5,7]
    lis2=[2,4,6,8]
    print(mergetwosorted(lis1,lis2))
    lis=[3,5,3,2,123,1,2,0]
    print(mergeorted(lis))
    #print(a)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
