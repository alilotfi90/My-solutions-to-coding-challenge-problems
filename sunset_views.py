def sunsetViews(buildings, direction):
    cansee=[]
    if direction=="WEST":
        for i in range(len(buildings)):
            if i==0:
                cansee.append(i)
                maxheight=buildings[i]
            else:
                if buildings[i]>maxheight:
                    cansee.append(i)
                    maxheight=buildings[i]
        return cansee
    if direction=="EAST":
        n=len(buildings)
        for i in range(len(buildings)-1,-1,-1):
            if i==n-1:
                cansee.append(i)
                maxheight=buildings[i]
            else:
                if buildings[i]>maxheight:
                    cansee.append(i)
                    maxheight=buildings[i]
        return cansee[::-1]