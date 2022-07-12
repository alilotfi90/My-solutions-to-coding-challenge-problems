def peak_of_mountain_array(arr):
    left , right = 0 , len(arr)-1
    ind=-1
    while left<=right:
        mid=(left+right)//2
        #is arr[mid]==True?
        if arr[mid]>arr[mid+1]:
            ind=mid
            right=mid-1
        else:
            left=mid+1
    return ind
def main():
    arr=[0,1,0]
    print(peak_of_mountain_array(arr))

if __name__ == "__main__":
  main()