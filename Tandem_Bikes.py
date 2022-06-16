#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Minimum_Waiting_Time.py
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
import operator
import math as m
def taskAssignment(k, tasks):
    tbs=[]
    retlis=[]
    for i in range(len(tasks)):
        tbs.append((tasks[i],i))
    tbs.sort()
    stl_tbs=tbs
    lts_tbs=tbs[::-1]
    n=len(tbs)
    for i in range(n//2):
        retlis.append([stl_tbs[-1][1],lts_tbs[-1][1]])
        stl_tbs.pop()
        lts_tbs.pop()
        
    return retlis
def main(args):
    #ds=sorted(d.items(), key=lambda x: x[0])
    #print(ds)
    tasks=[[15, 17],[19, 13],[8, 16],[2, 7],[12, 6],[11, 5],[3, 4],[0, 14],[1, 10],[18, 9]]
    k=len(tasks)//2
    print(taskAssignment(k,tasks))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
