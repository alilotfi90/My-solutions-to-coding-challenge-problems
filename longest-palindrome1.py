#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  memoized-matrix-chain.py
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
	s="cbbdb"
	rets=""
	rows, cols = (len(s), len(s))
	arr = [[False for i in range(cols)] for j in range(rows)]
	maxs=1
	for i in range(len(s)):
		arr[i][i]=True
	for i in reversed(range(len(s)-1)):
		for j in range(i+1,len(s)):
			if j==i+1:
				arr[i][j]= s[i]==s[j]
				if arr[i][j] and j-i+1>maxs:
					maxs=j-i+1
					rets=s[i:j+1]
			if j>=i+2:
				arr[i][j]= s[i]==s[j] and arr[i+1][j-1]
				if arr[i][j] and j-i+1>maxs:
					maxs=j-i+1
					rets=s[i:j+1]
	print(maxs)
	print(rets)
	#if j==i+1:
	#			arr[i][j]= s[i]==s[j]
	#		elif j>=i+2:
	#			arr[i][j]= s[i]==s[j] and arr[i+1][j-1]
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
