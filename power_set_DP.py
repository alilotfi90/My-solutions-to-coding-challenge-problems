#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  power_set.py
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
def powerset(lis):
	if len(lis)==0:
		return []
	if len(lis)==1:
		return [[],[lis[0]]]
	n=len(lis)
	dp=[0 for i in range(n)]
	dp[0]=[[],[lis[0]]]
	for i in range(1,n):
		dp[i]=[a + [lis[i]] for a in dp[i-1]]+dp[i-1]
	#add lis[i] to all elements of dp[i-1] and also have a copy of dp[i-1]
	return dp[n-1]
def main(args):
    lis1=[1,2,3]
    print(powerset(lis1))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
