#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Partition_to_Two_Equal_Sum_Subsets.py
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
def canpart(nums,target):
    totsum=sum(nums)
    if len(nums)<2:
	return False
    if totsum % 2!=0:
	return False
    if max(nums)>target:
	return False
    midsum=totsum//2
    dp=[False]*(midsum+1)
    dp[0]=True
    for num in nums:
	for i in range(midsum,num-1,-1):
	    dp[i] = dp[i] or dp[i-num]
    return dp[midsum]
def main(args):
    target=8
    lis0=[1]
    lis=[1,2,2,4,2,5]
    print(canpart(lis,8))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
