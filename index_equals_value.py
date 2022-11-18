def indexEqualsValue(array):
    if len(array)==0:
        return -1
    if len(array)==1:
        if array[0]==0:
            return 0
        else:
            return -1
    n=len(array)
    l=0
    r=n-1
    while 0 <=l<=n-1 and 0 <= r <=n-1 and r>=l:
        if array[l]==l:
            return l
        mid=(l+r)//2
        if array[mid]<mid:
            l=mid+1
        elif array[mid]>mid:
            r=mid-1
        else:
            r=mid
    if array[mid]!=mid:
        return -1