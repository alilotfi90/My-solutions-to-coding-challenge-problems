#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Coin_Change.py
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
from math import inf
from typing import List

def coin_change(coins: List[int], amount: int) -> int:
    if amount==0:
        return 0
    dp=[inf]*(amount+1)
    dp[0]=0
    for i in range(1,amount+1):
        for coin in coins:
            if i-coin>=0:
                dp[i]=min(dp[i],1+dp[i-coin])
    if dp[-1]<inf:
        return dp[-1]
    else:
        return -1

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
