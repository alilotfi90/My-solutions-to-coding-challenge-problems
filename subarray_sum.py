from typing import Counter
def subarray_sum(arr,target):
    dic={0:0}
    cursum=0
    for i in range(len(arr)):
        cursum+=arr[i]
        dic[cursum]=i+1
        if cursum-target in dic:
            return [dic[cursum-target],i+1]
def main(args):
	lis , target = [0,1,2,3,4] , 6
	print(subarray_sum(lis,target))

''
if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))