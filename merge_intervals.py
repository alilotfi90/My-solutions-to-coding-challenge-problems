def do_intersect(a,b):
    if len(a)!=2 or len(b)!=2 or max(a[0],b[0])>min(a[1],b[1]):
        return False
    else:
        return [min(a[0],b[0]),max(a[1],b[1])]
def merge_interval(lis):
    lis.sort(key=lambda x:x[0])
    res=[]
    for interval in lis:
        if not res or not do_intersect(res[-1],interval):
            res.append(interval)
        else:
            a=do_intersect(res[-1],interval)
            res.pop()
            res.append(a)
    return res
def main(args):
    interval1=[1,2]
    interval2=[2,4]
    print(do_intersect(interval1,interval2))
    lis=[[1,2],[2,4],[5,6]]
    lis.sort(key=lambda x:x[1])
    print(merge_interval(lis))
    #print(lis)
    #print(lis[-1])
    #print(lis)
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
