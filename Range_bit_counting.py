#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  temp2.py
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
#   Range Bit Counting
#  
def range_bit_count(a, b):
    count=0
    for i in range(a,b+1):
        st1=bin(i)
        st2=st1[2:len(st1)]
        for i in range(0,len(st2)):
            if int(st2[i])==1:
                count=count+1
    return count    
    #coding and coding..
def main(args):
	print("This code is for Range Bit Counting")
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
