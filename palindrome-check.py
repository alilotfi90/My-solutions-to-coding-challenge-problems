#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  palindrome-check.py
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

def isPalindrome(string):
    if len(string)==0:
        return True
    if len(string)==1:
        return True
    if string[0]==string[-1]:
        return isPalindrome(string[1:-1])
    else:
        return False
def main(args):
	pal='aba'
	notpal='abc'
	print(isPalindrome(pal)) 
	print(isPalindrome(notpal))
	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
