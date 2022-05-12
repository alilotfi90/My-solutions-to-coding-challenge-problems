#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  merge.py
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
def mergetwo(x,y):
	z=[]
	i=0
	j=0
	while i < len(x) or j < len(y):
		if j==len(y) or (i < len(x) and x[i]<=y[j]):
			z.append(x[i])
			i+=1
		else:
			z.append(y[j])
			j+=1
	return z

def main(args):
    print(complex(1,2)+complex(2,3))
    str1="pro1"
    str2="pro13"
    print(str1 and str2)
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
