from typing import List
from collections import deque
def shortest_path(graph, a, b):
    if a==b:
        return 0
    queue=deque([a])
    visited=set()
    dist=0
    while len(queue)!=0:
        n=len(queue)
        for i in range(n):
            newvert=queue.popleft()
            visited.add(newvert)
            if newvert==b:
                return dist
            for neigh in graph[newvert]:
                if neigh not in visited:
                    queue.append(neigh)
                    visited.add(neigh)
        dist+=1
def main():
    graph=[[1,2],[2,3],[3],[0]]
    a=0
    b=3
    print(shortest_path(graph, a, b))
    
if __name__ == "__main__":
  main()