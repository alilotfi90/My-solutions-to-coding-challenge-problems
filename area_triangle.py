#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  area_triangle.py
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
#  


def main(args):
	# Python Program to find the area of triangle
	
	a = float(input('Enter first side: '))
	b = float(input('Enter second side: '))
	c = float(input('Enter third side: '))

	# calculate the semi-perimeter
	s = (a + b + c) / 2

	# calculate the area
	area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
	print('The area of the triangle is %0.2f' %area)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
