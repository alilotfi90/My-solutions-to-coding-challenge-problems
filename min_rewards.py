def minRewards(scores):
    if len(scores)==1:
        return 1
    n=len(scores)
    reward=[0 for i in range(n)]
    for i in range(n):
        if i==0:
            reward[i]=1
            continue
        if scores[i]>scores[i-1]:
            reward[i]=reward[i-1]+1
            continue
        #reward[i]<reward[i-1]
        reward[i]=1
        for j in range(i-1,-1,-1):
            if scores[j]<scores[j+1]:
                break
            else:
                reward[j]=max(reward[j+1]+1,reward[j])
    return sum(reward)