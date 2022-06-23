def find_all_anagrams(original, check):
    st1=original
    st2=check
    retlis=[]
    dicnf={}
    for a in st1[0:len(st2)]:
        dicnf[a]=st1[0:len(st2)].count(a)
    dicf={}
    for a in st2:
        dicf[a]=st2.count(a)
    count=0
    if dicf==dicnf:
        retlis.append(0)
    for i in range(0,len(st1)-len(st2)):
        dicnf[st1[i]]-=1
        if st1[i+len(st2)] in dicnf.keys():
            dicnf[st1[i+len(st2)]]+=1
        else:
            dicnf[st1[i+len(st2)]]=1
        dicnf={key:dicnf[key] for key in dicnf if dicnf[key]!=0}
        if dicnf==dicf:
            retlis.append(i+1)
    return retlis
def main(args):
	st1="stringtocheck"
	st2="check"
	
	print(find_all_anagrams(st1, st2))
		
''
if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))