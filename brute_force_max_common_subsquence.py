#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  brute_force_max_common_subsquence.py
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

def brforcesubseq(lis1,lis2):
	if len(lis1)>len(lis2):
		return False
	elif len(lis1)==0:
		return True
	else:
		return (lis1[0] in lis2) and brforcesubseq(lis1[1:],lis2)
def main(args):
    lis1=[1,2]
    lis2=[1,4,3]
    print(brforcesubseq(lis1,lis2))
		
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
