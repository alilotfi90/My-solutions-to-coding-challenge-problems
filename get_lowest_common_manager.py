def countsub(top, reportOne, reportTwo):
    if len(top.directReports)==0:
        if top.name==reportOne.name or top.name==reportTwo.name:
            return 1
        else:
            return 0
    sum=0
    if top.name==reportOne.name or top.name==reportTwo.name:
        sum=1
    for sub in top.directReports:
        sum+=countsub(sub, reportOne, reportTwo)
    return sum
def getLowestCommonManager(topManager, reportOne, reportTwo):
    consider=topManager
    if countsub(consider, reportOne, reportTwo)==2:
        allfalse=True
        for sub in consider.directReports:
            if countsub(sub, reportOne, reportTwo)==2:
                allfalse=False
        if allfalse==True:
            return consider
    for subconsider in consider.directReports:
        if  countsub(subconsider, reportOne, reportTwo)==2:
            return getLowestCommonManager(subconsider, reportOne, reportTwo)


# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []