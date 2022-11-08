def tournamentWinner(competitions, results):
    dic={}
    maxstr=""
    maxscore=0
    for i in range(len(competitions)):
        if results[i]==1:
            if competitions[i][0] in dic:
                dic[competitions[i][0]]+=3
            else:
                dic[competitions[i][0]]=3
            if dic[competitions[i][0]]>maxscore:
                maxstr=competitions[i][0]
                maxscore=dic[competitions[i][0]]
        else:
            if competitions[i][1] in dic:
                dic[competitions[i][1]]+=3
            else:
                dic[competitions[i][1]]=3
            if dic[competitions[i][1]]>maxscore:
                maxstr=competitions[i][1]
                maxscore=dic[competitions[i][1]]
    return maxstr