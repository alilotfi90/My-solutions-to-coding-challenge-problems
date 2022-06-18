#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bubble_sort.py
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
def bubbleSort(array):
    bo=True
    while bo:
        bo=False
        for i in range(len(array)-1):
            if array[i+1]<array[i]:
                array[i+1] , array[i] = array[i] , array[i+1]
                bo=True
    return array

def main(args):
    array=[1,-1,2,3,-5]
    print(bubbleSort(array))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
