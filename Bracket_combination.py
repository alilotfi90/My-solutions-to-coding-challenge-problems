#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  temp1.py
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
# We count the number of bracket combinations. 
# num is the input and we count the number of logically sensibile expressions. With Num many { and Num many }

def countbrac(num):
	ret=1
	if num==0:
		return ret
	elif num==1:
		return ret
	else:
		sum1=0
		for i in range(1,num+1):
			sum1=sum1+countbrac(i-1)*countbrac(num-i)
	return sum1
def main(args):
	
	print(countbrac(3))

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
