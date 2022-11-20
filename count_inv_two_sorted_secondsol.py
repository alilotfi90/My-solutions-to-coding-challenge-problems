def countInversions(array):
    return countinvsubarray(array,0,len(array))
def countinvsubarray(array,start,end):
    if end-start<=1:
        return 0
    # mid=start + (end-start)//2
    mid=(start + end)//2
    
    leftinv=countinvsubarray(array,start,mid)
    rightinv=countinvsubarray(array,mid,end)
    mergarrinv=mergesortandcountinv(array,start,mid,end)
    return leftinv+rightinv+mergarrinv
def mergesortandcountinv(array,start,mid,end):
    sortedarr=[]
    left=start
    right=mid
    invs=0
    print(array[start:mid])
    print(array[mid:end])
    while left<mid and right<end:
        if array[left]<=array[right]:
            sortedarr.append(array[left])
            left+=1
        else:
            invs+=mid-left
            sortedarr.append(array[right])
            right+=1
    sortedarr+=array[left:mid]+array[right:end]
    for id , vals in enumerate(sortedarr):
        array[start+id]=vals
    return invs
    