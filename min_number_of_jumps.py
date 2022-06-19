#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  min_number_of_jumps.py
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
def minNumberOfJumps(array):
    dp=[0 for i in range(len(array))]
    for i in range(1,len(array)):
        dp[i]=float('inf')
        for j in range(0,i):
            if j+array[j]>=i:
                dp[i]=min(dp[i],dp[j]+1)
    return dp[len(array)-1]

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
