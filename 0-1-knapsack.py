#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  0-1-knapsack.py
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
def knapsack(weights, values, max_weight):
    cols=max_weight
    rows=len(weights)
    if cols==0 or rows==0:
        return 0
    dp=[[0 for i in range(cols+1)] for j in range(rows)]
    #first row is when nothing to rob, first column is when max_weight is zero
    for i in range(rows):
        dp[i][0]=0
    for i in range(cols+1):
        if i>=weights[0]:
            dp[0][i]=values[0]
        else:
            dp[i][0]=0
    for j in range(1,cols+1):
        for i in range(1,rows):
            dp[i][j]=dp[i-1][j]
            if j-weights[i]>=0:
                dp[i][j]=max(dp[i-1][j],values[i]+dp[i-1][j-weights[i]])
    return dp[rows-1][cols]

def main(args):
    weights=[3,4,7]
    values=[4,5,8]
    maxweight=7
    print(knapsack(weights,values,maxweight))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
