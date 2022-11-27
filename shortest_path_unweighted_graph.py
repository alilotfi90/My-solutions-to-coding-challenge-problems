from typing import List
from collections import deque

def bfs(graph,root,des):
    queue = deque([root])
    visited = {root:0}
    while len(queue) > 0:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor in visited:
                continue
            queue.append(neighbor)
            visited[neighbor]=visited[node]+1
    return visited[des]
def shortest_path(graph: List[List[int]], a: int, b: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    return bfs(graph,a,b)