white, grey, black = 0 , 1, 2
def cycleInGraph(edges):
    colors=[white for i in range(len(edges))]
    for node in range(len(edges)):
        if colors[node]!=white:
            continue
        containscycle=travandcolor(edges,node,colors)
        if containscycle:
            return True
    return False
def travandcolor(edge,node,colors):
    colors[node]=grey
    neighbors=edge[node]

    for neighbor in neighbors:
        if colors[neighbor]==grey:
            return True
        if colors[neighbor]!=white:
            continue
        containscycle=travandcolor(edge,neighbor,colors)
        if containscycle:
            return True
    colors[node]=black
    return False
def main():
    edge=[[1],
    [2],
    [3],
    [4],
    [5],
    []
    ]
    #print(edge)
    print(cycleInGraph(edge))


    
if __name__ == "__main__":
  main()