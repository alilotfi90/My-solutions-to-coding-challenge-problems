def find_min_rotated(arr):
    n=len(arr)
    left , right = 0 , n-1
    mid=(left+right)//2
    while left<right:
        mid=(left+right)//2
        if arr[mid]<arr[right] and arr[left]<arr[mid]:
            return left
        if arr[mid]<arr[right]:
            right=mid-1
            continue
        if arr[mid]>arr[right]:
            left=mid+1
            continue
    return mid
def main():
    arr=[4,5,6,7,8,1,2]
    print(find_min_rotated(arr))

if __name__ == "__main__":
  main()