from typing import List
from heapq import heappop, heappush
from math import sqrt
# given a set of points, this calculates the closest k points to the origin
def k_closest_points(points, k):
    heap=[]
    res=[]
    for point in points:
        heappush(heap, (sqrt(point[0] ** 2 + point[1] ** 2), point))
    for i in range(k):
        res.append(heappop(heap)[1])
    return res