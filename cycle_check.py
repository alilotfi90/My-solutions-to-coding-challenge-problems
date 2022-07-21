def hasSingleCycle(array):
    n=len(array)
    visited=set()
    vert=0
    count=0
    while vert not in visited:
        visited.add(vert)
        count+=1
        vert=(array[vert]+vert)%n
    if count==n and vert==0:
        return True
    else:
        return False
def main():
    cyc=[1,1,1,1]
    noncyc=[1,1,1,2]
    print(hasSingleCycle(cyc))
    print(hasSingleCycle(noncyc))
if __name__ == "__main__":
  main()