def shiftedBinarySearch(array, target):
    left , right = 0 , len(array)-1
    while left<=right:
        mid=(left+right)//2
        if array[mid]==target:
            return mid
        if array[mid]<=array[right]:
            if array[mid]<target and target<=array[right]:
                left=mid+1
                ind=mid+1
                continue
            else:
                right=mid-1
                ind=mid-1
                continue
        else:
            if target<array[mid] and array[left]<=target:
                right=mid-1
                continue
            else:
                left=mid+1
                ind=mid+1
    if array[ind]==target:
        return ind
    else:
        return -1
def main():
    lis=[1,2,-5,-4,-3,-2]
    print(shiftedBinarySearch(lis, 2))
if __name__ == "__main__":
  main()