#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Longest_Peak.py
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
def threepeak(a,b,c):
	if a<b and b>c:
		return True
	return False
def longestPeak(array):
    n=len(array)
    mid=1
    maxlen=0
    while mid<=n-2:
        lis=[array[mid]]
    	if threepeak(array[mid-1],array[mid],array[mid+1]):
    	    left = mid
    	    while left>0 and array[left-1]<array[left]:
    		    lis=[array[left-1]]+lis
    		    left=left-1
    	    right = mid
    	    while right<=n-2 and array[right]>array[right+1]:
    		    lis=lis+[array[right+1]]
    		    right=right+1		
    	maxlen=max(maxlen,len(lis))
    	mid=mid+1 
    if maxlen<=2:
        return 0
    return maxlen

def main(args):
    array=[1,2,3,3,4,0,10,6,5,-1,-3,2,3]
    print(longestPeak(array))
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
