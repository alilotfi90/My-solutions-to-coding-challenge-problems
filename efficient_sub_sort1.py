def out_of_order_index(array):
    n=len(array)
    res=[]
    for i in range(1,n):
        if array[i-1]>array[i]:
            res.append(i-1)
            res.append(i)
    if len(res)==0:
        return False
    lis=list(set(res))
    minind , maxind = lis[0] ,lis[0]
    minval , maxval = array[minind] , array[maxind]
    for ind in lis:
        if array[ind]<minval:
            minind=ind
            minval=array[minind]
        if array[ind]>maxval:
            maxind=ind
            maxval=array[maxind]
    return [(minind,minval),(maxind,maxval)]
def subarraySort(array):
    if len(array)<=1:
        return array
    if not out_of_order_index(array):
        return [-1,-1]
    #minind=[(minind,minval),(maxind,maxval)][0][0]
    #maxind=[(minind,minval),(maxind,maxval)][1][0]
    minind=out_of_order_index(array)[0][0]
    maxind=out_of_order_index(array)[1][0]
    #print(minind)
    #print(maxind)
    for i in range(len(array)):
        if array[i]<=array[minind]:
            continue
        else:
            aftermin=i
            print('afterminis',aftermin)
            break
    for i in range(len(array)-1,-1,-1):
        print('i is',i)
        if array[i]>=array[maxind]:
            continue
        else:
            aftermax=i
            break
    return [aftermin,aftermax]
def efficient_subsort(array):
    return True
    
def main():
    array=[1,2,4,7,10,11,7,12,7,7,16,18,19]
    print(array)
    print(out_of_order_index(array))
    minind=out_of_order_index(array)[0][0]
    maxind=out_of_order_index(array)[1][0]
    print(minind)
    print(maxind)
    templis1=array[::]
    templis2=array[::]
    print(subarraySort(array))
        
    #print(subarraySort(array))
    #array.sort()
    #print(array)


if __name__ == "__main__":
  main()