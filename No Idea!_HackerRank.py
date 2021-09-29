#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  No Idea!_HackerRank.py
#  
#  Copyright 2021 Ali Lotfi <ali@ali-Oryx-Pro>
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
# Solution to Problem "No Idea!" from HackerRank.
def calculate_happines():
	m, n = map(int , input().split())
	lis=[int(x) for x in input().split()]
	A=set([int(x) for x in input().split()])
	B=set([int(x) for x in input().split()])
	happi=0
	for a in lis:
		if a in A:
			happi+=1
		if a in B:
			happi-=1        
	print(happi)
	
  


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
