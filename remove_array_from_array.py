#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled1.py
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
def array_diff(a, b):
    print(b)
    myList = a
    valueToBeRemoved=b
    result = filter(lambda val: val not in  valueToBeRemoved, myList) 
    return list(result)
    #your code here
def main(args):
	#print("hi")
	#a=[1 ,2 ,3, 5]
	#b=[1 ,5 ,6 ,7]
	#lst3 = [value for value in a if value in b]
	#print(lst3)
	myList = [2, 1, 3, 5, 1, 1, 1, 0]
	valueToBeRemoved = [1, 5]
	#array_diff([1,2],[1])
	result = filter(lambda val: val not in  valueToBeRemoved, myList) 
	print(list(result))
	#array_diff([1,2],[1,2,4])
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
