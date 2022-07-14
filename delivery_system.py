def check_possible(weight1,truck_max_weight,d):
  weight=weight1[:]
  if len(weight)==0:
    return True
  retlis=[]
  while len(weight)!=0:
    if len(retlis)>d:
      return False
    templis=[]
    while len(weight)!=0 and sum(templis)+weight[-1]<=truck_max_weight:
      a=weight.pop()
      templis.append(a)
    retlis.append(templis)
  if len(retlis)>d:
    return False
  else:
    return True
def min_max_weight(weights,d):
    boudary={}
    for i in range(max(weights),sum(weights)+1):
        boudary[i]=False
    left , right = max(weights) , sum(weights)
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        #print(weights,mid,d)
        if check_possible(weights,mid,d):
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index
def main():
    weights=[1,2,3,4,5,6,7,8,9,10]
    d=5
    print(min_max_weight(weights,d))
if __name__ == "__main__":
  main()