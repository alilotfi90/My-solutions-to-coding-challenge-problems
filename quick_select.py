def quickhelper(array,start,end):
    if start>=end:
        return start
    piv=start
    left=start+1
    right=end
    while right>=left:
        if array[left]>array[piv] and array[piv]>array[right]:
            array[left] , array[right] = array[right] , array[left]
        if array[left]<=array[piv]:
            left+=1
        if array[right]>=array[piv]:
            right-=1
    array[right] , array[piv] = array[piv] , array[right]
    return right
def quickselect(array, k):
    if k>len(array):
        return
    start=0
    end=len(array)-1
    piv=quickhelper(array,start,end)
    if piv==k-1:
        return array[piv]
    elif piv>k-1:
        return quickselect(array[:piv],k)
    else:
        return quickselect(array[piv+1:],k-(piv+1))