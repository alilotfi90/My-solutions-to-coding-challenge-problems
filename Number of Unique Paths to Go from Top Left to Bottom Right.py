#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test.py
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
def unique_paths(m, n):
    dp=[[0 for i in range(n)] for j in range(m)]
    dp[0]=[1 for i in range(n)]
    for i in range(1,m):
        for j in range(n):
            if j==0:
                dp[i][j]=1
            else:
                dp[i][j]=dp[i][j-1]+dp[i-1][j]
                
    return dp[m-1][n-1]

def main(args):
	m=3
	n=2
	print(unique_paths(m, n))
	return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
