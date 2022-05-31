#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  activity_selection_problem.py
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
def inbetween(a1,a2,a3):
	if a1[1]<=a2[0] and a2[1]<=a3[0]:
		return True
	else:
		return False
# S is the set of activities, its elements are of the form (s_i,f_i) where s_i and f_i are start and finish respectively
# Let SI be a two dimentiosla array such that SI[i][j] is the set of events such that start after a_i and ends before, a_j 
def main(args):
    S=[(-2,0),(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(8,12),(2,14),(12,16),(float('inf'),float('inf'))]
    n=len(S)-2
    c=[[0 for x in range(n+2)] for y in range(n+2)]
    act=[[0 for x in range(n+2)] for y in range(n+2)]
    print("size is",n)
    for i in range(n+1):
	c[i][i]=0
	c[i][i+1]=0
    c[n+1][n+1]=0
    for l in range(2,n+2):
	for i in range(0,n-l+2):
	    j=i+l
	    c[i][j]=0
	    k=j-1
	    while S[i][1]<S[k][1]:
		if inbetween(S[i],S[k],S[j]) and c[i][k]+c[k][j]+1>c[i][j]:
		    c[i][j]=c[i][k]+c[k][j]+1
		    act[i][j]=k
		k=k-1
    print(c[0][n+1])
    print(act[0][n+1])
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
