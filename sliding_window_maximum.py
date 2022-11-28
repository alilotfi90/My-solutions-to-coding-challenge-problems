from collections import deque
from typing import List

def sliding_window_maximum(nums, k):
    q = deque()
    res = []
    for i, cur in enumerate(nums):
        while q and cur>=nums[q[-1]]:
            q.pop()
        q.append(i)
        
        # we are index i, therefore, the window is [i-k+1,...,i-1,i], meaning we need to make sure i-k is not in q
        if q[0]==i-k:
            q.popleft()
        if i>=k-1:
            res.append(nums[q[0]])
    return res

nums=[1,2,4,3,2,5,3]
k=3
print(sliding_window_maximum(nums, k))
