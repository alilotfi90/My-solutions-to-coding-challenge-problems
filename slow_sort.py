#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  slow_sort.py
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
#  GNU General Public License for more details.s
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import numpy as np

def main(args):
	lis=[1,2,3,5,23,1,2,1,2]
	for i in range(len(lis)):
		for j in range(i,len(lis)):
			if lis[i]>lis[j]:
				x=lis[i]
				lis[i]=lis[j]
				lis[j]=x
	print(lis)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
