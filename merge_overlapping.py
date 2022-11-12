# merges overlapping intervals
def mergeOverlappingIntervals(intervals):
    intervals.sort(key=lambda x: int(x[0]))
    ind=0
    lenlis=len(intervals)
    print(intervals)
    while ind<=lenlis:
        if ind==lenlis-1:
            return intervals
        if intervals[ind][1]>=intervals[ind+1][0]:
            intervals[ind]=[intervals[ind][0],max(intervals[ind][1],intervals[ind+1][1])]
            del intervals[ind+1]
            lenlis-=1
        else:
            ind+=1