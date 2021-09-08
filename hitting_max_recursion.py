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
import time
def fact(n):
  if n==0:
	  fac=1
  else:
	  fac=n*fact(n-1)
  return fac
def main(args):
	start=time.time()
	n=1e3
	print(fact(n))
	
	end=time.time()
	spent=end-start
	print("the time spent",spent)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
