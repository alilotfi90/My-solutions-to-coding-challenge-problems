def levenshteinDistance(str1, str2):
    if len(str1)==0 or len(str2)==0:
        return max(len(str1),len(str2))
    m=len(str1)+1
    n=len(str2)+1
    matrix=[[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        matrix[0][i]=i
    for i in range(1,m):
        matrix[i][0]=i
    for i in range(1,m):
        for j in range(1,n):
            if str1[i-1]==str2[j-1]:
                matrix[i][j]=min(matrix[i][j-1]+1,matrix[i-1][j]+1,matrix[i-1][j-1])
            else:
                matrix[i][j]=min(matrix[i][j-1]+1,matrix[i-1][j]+1,matrix[i-1][j-1]+1)
    return matrix[m-1][n-1]