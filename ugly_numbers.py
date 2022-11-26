from heapq import heappop, heappush
def nth_ugly_number(n: int) -> int:
    heap=[1]
    used_numbers={1}
    allowedprimes=(2,3,5)
    # 1st number is 1
    for i in range(n-1):
        val=heappop(heap)
        for mult in allowedprimes:
            if mult*val not in used_numbers:
                heappush(heap,mult*val)
                used_numbers.add(mult*val)
    
        
    return heappop(heap)