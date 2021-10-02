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
#   
#  
import math
import sympy
import random as ran


def main(args):
	rg=ran.randint(1, 100)
	print("I'm thinking of a number between 0 and 100")
	n=-1
	atmpt=0
	while n!=rg:
		n=int(input("Enter your guess:"))
		atmpt=atmpt+1
		if n==rg:
			print("Good job!",n,"is my number.")
			print("It took you", atmpt ,"guesses.")
			return
		if n>rg:
			print("Sorry,",n,"is too high.")
		if n<rg:
			print("Sorry,",n,"is too low.")
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
