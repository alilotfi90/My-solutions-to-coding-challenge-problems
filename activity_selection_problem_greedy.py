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
def doesint(a1,a2):
	if a1[1]==a2[0]:
		return False
	if (a1[0] <= a2[0] and a2[0]<a1[1]) or (a2[0] <= a1[0] and a1[0]<a2[1]):
		return True
	return False
def greedy(S):
	retlis=[]
	count=1
	retlis.append(S[0])
	for i in range(1,len(S)):
		bo=True
		for a in retlis:
			if doesint(S[i],a):
				bo=False
		if bo:
			retlis.append(S[i])
			count=count+1
	return (retlis,count)
			
def main(args):
    S=[(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(8,12),(2,14),(12,16)]
    print(S)
    print(greedy(S))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
