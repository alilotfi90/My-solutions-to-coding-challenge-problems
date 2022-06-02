#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sorted_square_array.py
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


def main(args):
    arr=[-7,-5,-4,3,6,8,9]
    start=0
    end=len(arr)-1
    retarr=[0]*len(arr)
    count=len(arr)-1
    while count>=0:
	if abs(arr[end])>=abs(arr[start]):
	    retarr[count]=(arr[end])**2
	    end-=1
	else:
	    retarr[count]=(arr[start])**2
	    start+=1
	count-=1
    print(retarr)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
