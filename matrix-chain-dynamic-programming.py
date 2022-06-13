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
def matrchain(p,m,n):
	le=len(p)
	dp=[[0 for i in range(le)] for j in range(le)]
	tr=[[0 for i in range(le)] for j in range(le)]
	# Product matrix will be A_{1} ... A_{le -1}
	# length of the product could be from dp[0][i] should remain 0
	# for 1<= i <= le-1 and i<=j<=le-1, dp[i][j] is the optimal number for A_{i} ... A_{j}
	# let l be size of the chain, min(l)=2, length of A_{i}...A_{j} is j-i+1, therefore, max of l is when i=1, j=le-1, and j-i+1 is le-1-1+1=le-1
	# l is in range(2,le)
	# given l, min i is 1, and max is when j=le-1, therefore, i+l-1=le-1, giving us i=le-l. 
	# Therefore, i is in range(1,le-l+1)
	for i in range(1,le-1):
		tr[i][i]=i
	for i in range(1,le-1):
		tr[i][i+1]=i
	for l in range(2,le):
		for i in range(1,le-l+1):
			j=i+l-1
			dp[i][j]=float('inf')
			for k in range(i,j):
				if dp[i][j]>dp[i][k]+dp[k+1][j]+p[i-1]*p[k]*p[j]:
					dp[i][j]=dp[i][k]+dp[k+1][j]+p[i-1]*p[k]*p[j]
					tr[i][j]=k
	return (dp[m][n],tr[m][n])
	#return tr
def main(args):
	p=[10,20,30,10,40,5,43,2323,123,23]
	m=1
	n=len(p)-1
	print(matrchain(p,m,n))
	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
