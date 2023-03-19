import heapq
def sortKSortedArray(array, k):
    min_heap = []
    n=len(array)

    retlis=[]
    for i in range(n):
        heapq.heappush(min_heap,array[i])
        if i>=k:
            to_add = heapq.heappop(min_heap)
            retlis.append(to_add)
    while len(min_heap)!=0:
        to_add=heapq.heappop(min_heap)
        retlis.append(to_add)
    return retlis


