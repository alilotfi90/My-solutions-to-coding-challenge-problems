from typing import List
from heapq import heapify, heappop , heappush
def find_kth_largest(nums: List[int], k: int) -> int:
    res=[]
    heap=[]
    for i in range(k):
        heappush(heap, nums[i])
    for j in range(k,len(nums)):
        a=heappop(heap)
        if nums[j]<=a:
            heappush(heap,a)
            continue
        else:
            heappush(heap,nums[j])
            
    return heappop(heap)