from typing import List
from heapq import heappop, heappush
def kth_smallest(matrix: List[List[int]], k: int) -> int:
    res=[]
    heap=[]
    for cur in matrix:
        heappush(heap,(cur[0],cur,0))
    count=0
    while heap and count<k:
        val , cur_list , head_index = heappop(heap)
        count+=1
        if count==k:
            return val
        head_index+=1
        if head_index<len(cur_list):
            heappush(heap, (cur_list[head_index],cur_list,head_index))