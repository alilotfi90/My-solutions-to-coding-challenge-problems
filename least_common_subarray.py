#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  least_common_subarray.py
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
def lcs(X,Y):
    m=len(X)
    n=len(Y)
    c=[[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1,m+1):
	for j in range(1,n+1):
	    if X[i-1]==Y[j-1]:
		c[i][j]=c[i-1][j-1]+1
	    elif c[i-1][j]>=c[i][j-1]:
		c[i][j]=c[i-1][j]
	    else:
		c[i][j]=c[i][j-1]
    return c[m][n]

def main(args):
    X=[1,2,4,2,1]
    Y=[1,2,5,2,1]
    print(lcs(X,Y))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
