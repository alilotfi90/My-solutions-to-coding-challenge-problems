from random import random
from typing import List
import time
# Ali Lotfi, Design and Analysis of Algorithms
# k_vertex approximation algorithm
def k_vertex_approx(num_vert,graph):
    # visited is a dictionary which represents the vertices we have covered
    #if visited[i]=1, it means that either i is an element of our cover, or there exists j such that i is connected to j and j is in cover set
    visited={}
    # cover set represents the set of vertices that belong to our cover
    cover=set()
    # looping over the vertices(vert), which belong to the set {0,1,2,...,num_vert-1}
    for vert in range(num_vert):
        # if vert is not in cover nor it is connected to a vertex which is in the cover, then we add it to our dictionary
        if vert not in visited:
            # add vert to our cover since vert has not been visited
            cover.add(vert)
            # we add vert to visited dictionary
            visited[vert]=1
            # if vert is not connected to any vertex, then we simply need to add it to the cover, then go to next vertex in the list
            if vert not in graph:
                continue
            else:
                # if vert is connected to some other vertices, then we loop over all of it's neighbors
                for neighbor in graph[vert]:
                    # if neighbor of vert is not part of the visited vertices, then we add it
                    if neighbor not in visited:
                        visited[neighbor]=1
    return len(cover)
# the implementation of brute force function requires k_subsets function
# finding subsets of the list nums of size k
def k_subsets(nums,k):
    n = len(nums)
    res = []
    def dfs(i, cur,count):
        if count==k:
            res.append(cur)
            return
        if i==n:
            return
        #res.append(cur + [nums[i]])
        dfs(i + 1, cur,count)
        count+=1
        dfs(i + 1, cur + [nums[i]],count)
        
    dfs(0, [],0)
    return res
def brute_force_decide_k(num_vert,graph,k):
    if k==0:
        return 0
    vert_list=[i for i in range(num_vert)]
    k_perm_list=k_subsets(vert_list,k)
    for cover_choice in k_perm_list:
        m=1
        for v1 in vert_list:
            if v1 in cover_choice:
                continue
            else:
                if v1 in graph:
                    m=0
                    for v2 in graph[v1]:
                        if v2 in cover_choice:
                            m=1
        if m==1:
            return 1
    return 0
def brute_force_decide(num_vert,graph):
    for k in range(num_vert):
        if brute_force_decide_k(num_vert,graph,k)==1:
            print("minimum vertex cover using the brute force algorithm is", k)
            return
def main():
    print("experiment starts here:")
    min_num_vertex=100
    max_num_vertex=1000
    for num_vert in range(min_num_vertex,max_num_vertex):
        graph={}
        for i in range(num_vert):
            graph[i]=[]
        for i in range(num_vert):
            # graph[i]=[]
            for j in range(num_vert):
                if i!=j:
                    x=random()
                    if x<1/2 and j not in graph[i]:
                        graph[i].append(j)
                        graph[j].append(i)
        start1=time.time()
        print("\n")
        brute_force_decide(num_vert,graph)
        end1=time.time()
        print("time it took for brute force on complete graph on",num_vert,"vertices is",end1-start1)

        start2=time.time()
        k_vertex_approx(num_vert,graph)
        # brute_force_decide(num_vert,graph)
        end2=time.time()
        print("time it took for approximate complete graph on",num_vert,"vertices is",end2-start2)
    

if __name__ == "__main__":
  main()