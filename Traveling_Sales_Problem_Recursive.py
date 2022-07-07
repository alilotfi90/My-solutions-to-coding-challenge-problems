import numpy as np
def TSP_helper(distances,check,start,end,memo={}):
  minimum=np.inf
  for i in range(len(distances)):
    if i!=start and i!=end and i not in check:
      check[i]=1
      minimum=min(minimum,distances[start][i]+TSP_helper(distances,check,i,end))
      del check[i]
  if minimum==np.inf:
    return distances[start][end]
  return minimum

  return 0
def TSP(distances):
  check={}
  minval=np.inf
  for i in range(len(distances)):
    minval=min(minval,TSP_helper(distances,check,i,i))
  return minval 

def main():
    dist=[[0,10,20],[12,0,10],[19,11,0]]
    print(TSP(dist))

if __name__ == "__main__":
  main()