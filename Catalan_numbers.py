#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Catalan_numbers.py
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
def catalan(n):
  dp=[0 for i in range(n+1)]
  if n==0:
    dp[0]=1
    return 1
  if n==1:
    dp[1]=1
    return 1
  dp[0] , dp[1] = 1 , 1
  for i in range(2,n+1):
    for j in range(i):
      dp[i]=dp[i]+dp[j]*dp[i-1-j]
  return dp[n]

def main(args):
    print(catalan(10))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
