from collections import deque
def get_neighbors(coord):
    res = []
    row, col = coord
    delta_row = [-2, -2, -1, 1, 2, 2, 1, -1]
    delta_col = [-1, 1, 2, 2, 1, -1, -2, -2]
    for i in range(len(delta_row)):
        r = row + delta_row[i]
        c = col + delta_col[i]
        res.append((r, c))
    return res
def get_knight_shortest_path(x,y):
    if x==0 and y==0:
        return 0
    queue=deque([(0,0)])
    visited=set()
    dist=0
    
    while len(queue)!=0:
        # size of this level?--->n=len(queue)
        # loop over all this level's nodes, they are all not in visited, check if they are (x,y)
        # for each iteration, we loop over all neighbors and add them to queue if they are not visited
        # update dis
        
        n=len(queue)
        for _ in range(n):
            newnode=queue.popleft()
            visited.add(newnode)
            
            #rint(newnode[0],newnode[1])
            if newnode[0]==x and newnode[1]==y:
                return dist
            
            for neigh in get_neighbors(newnode):
                if neigh in visited:
                    continue
                queue.append(neigh)
        dist+=1
def main():
    print(get_knight_shortest_path(10,10))
if __name__ == "__main__":
  main()