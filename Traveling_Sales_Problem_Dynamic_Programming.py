import numpy as np
def TSP_helper(distances,check,index,end,memo={}):
	# we want a tuple of vertices checked, also the last vertex (tuple(check),index)
	# since we don't care about the order of indeces checked, sort(tuple)
	checked=tuple(sorted(check.keys()))
	if (checked,index) in memo:
		return memo[(checked,index)]
	minimum=np.inf
	for i in range(len(distances)):
		if i!=index and i!=end and i not in check:
			check[i]=1
			minimum=min(minimum,distances[index][i]+TSP_helper(distances,check,i,end,memo))
			del check[i]
	if minimum==np.inf:
		return distances[index][end]
	memo[(checked,index)]=minimum
	return memo[(checked,index)]
def TSP(distances):
  check={}
  memo={}
  minval=np.inf
  for i in range(len(distances)):
    minval=min(minval,TSP_helper(distances,check,i,i,memo))
  return minval
def main():
    dist=[[0,10,20],[12,0,10],[19,11,0]]
    print(TSP(dist))
if __name__ == "__main__":
  main()