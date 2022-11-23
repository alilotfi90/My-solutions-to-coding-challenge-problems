from typing import List
from collections import deque

def parentcount(graph):
    counts={i:0 for i in graph}
    for parent in graph:
        for node in graph[parent]:
            counts[node]+=1
    return counts
def toposort(graph,original):
    res=[]
    q=deque()
    count=parentcount(graph)
    for node in count:
        if count[node]==0:
            q.append(node)
    while len(q)>0:
        if len(q)>1:
            return False
        pick=q.popleft()
        res.append(pick)
        for child in graph[pick]:
            count[child]-=1
            if count[child]==0:
                q.append(child)
    return original==res

def sequence_reconstruction(original: List[int], seqs: List[List[int]]) -> bool:
    n=len(original)
    graph={node:set() for node in range(1,n+1)}
    for seq in seqs:
        for i in range(len(seq)-1):
            so=seq[i]
            des=seq[i+1]
            graph[so].add(des)
    return toposort(graph,original)