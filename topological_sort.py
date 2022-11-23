# This is an input class. Do not edit.
from collections import deque
def parentdetector(jobs, deps):
    parent={i: 0 for i in jobs}
    
    for dep in deps:
        parent[dep[1]]+=1
    return parent
def topologicalSort(jobs, deps):
    res=[]
    q=deque()
    parent=parentdetector(jobs, deps)
    dic={}
    for dep in deps:
        if dep[0] in dic:
            dic[dep[0]].append(dep[1])
        else:
            dic[dep[0]]=[dep[1]]
    for job in jobs:
        if parent[job]==0:
            q.append(job)
    
    if len(q)==0:
        return []
    while len(q)>0:
        pick=q.popleft()
        res.append(pick)
        if pick not in dic:
            continue
        for child in dic[pick]:
            parent[child]-=1
            if parent[child]==0:
                q.append(child)
    if len(res)!=len(jobs):
        return []
    return res