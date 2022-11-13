def quickSort(array):
    quickhelper(array,0,len(array)-1)
    return array
def quickhelper(array,start,end):
    if start>=end:
        return
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
    smallleft= (right-1-start) < (end-(right+1))
    if smallleft:
        quickhelper(array,start,right-1)
        quickhelper(array,right+1,end)
    else:
        quickhelper(array,right+1,end)
        quickhelper(array,start,right-1)
    return array