def firstele(arr1,arr2):
	p1=0
	p2=0
	m=len(arr1)
	n=len(arr2)
	summax=0
	count=0
	secsum1=0
	secsum2=0
	#sum2+=arr2[p2]
	while p1<m or p2<n:
		if p1<m and p2<n and arr1[p1]==arr2[p2]:
			summax+=max(secsum1,secsum2)+arr1[p1]
			p1+=1
			p2+=1
			secsum1=0
			secsum2=0
			#print(summax)
			continue
		if p1==m or (p2!=n and arr2[p2]<arr1[p1]):
			secsum2+=arr2[p2]
			p2+=1
			continue
		else:
			secsum1+=arr1[p1]
			p1+=1
			continue
	summax+=max(secsum1,secsum2)
	return summax

def main(args): 
	lis1=[2,4,5,8,10]
	lis2=[4,6,8,9]
	print(firstele(lis1,lis2))
	
	#print(firstele(lis1,lis2))
	#lis=[1,2,3]
	#print(lis[3:]
''
if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))