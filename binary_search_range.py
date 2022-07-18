def binary_smallest_ind(array,target):
    left , right = 0 , len(array)-1
    ind=-1
    while left<=right:
        mid=(left+right)//2
        if array[mid]==target:
            if mid==0 or array[mid-1]!=target:
                return mid
            else:
                right=mid-1
        if array[mid]<target:
            left=mid+1
            ind=mid+1
            continue
        if array[mid]>target:
            right=mid-1
            ind=mid-1
            continue
    if array[ind]==target:
        return ind
    else:
        return -1
def binary_largest_ind(array,target):
    left , right = 0 , len(array)-1
    ind=-1
    while left<=right:
        mid=(left+right)//2
        if array[mid]==target:
            if mid==right or array[mid+1]!=target:
                return mid
            else:
                left=mid+1
        if array[mid]<target:
            left=mid+1
            ind=mid+1
            continue
        if array[mid]>target:
            right=mid-1
            ind=mid-1
            continue
    if array[ind]==target:
        return ind
    else:
        return -1
def binary_range(array,target):
    return [binary_smallest_ind(array,target),binary_largest_ind(array,target)]
def main():
    lis=[1,1,1,1,1,2,3,3,3,3,3,5,6,7,8,9,10]
    print(binary_range(lis, 3))
if __name__ == "__main__":
  main()